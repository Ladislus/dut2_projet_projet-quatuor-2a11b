from .views import *
from .forms import *
from .models import *

from .views_other import *

# @app.route("/stage/<int:id>")
# def stage_Id(id):
#     a = get_stages(id)
#     return render_template("stage.html",
#             title=a.intituleSt)


@app.route("/stage/presentation/", methods = ["GET", "POST"])
def stage_presentation():
    """

    :return: Retourne le template de la page de presentation de stage
    """
    return render_template("stage/stage_presentation.html", dico_stage=get_stages())

@app.route("/stage/inscription/", methods = ["GET", "POST"])
def stage_inscription():
    """

    :return: Retourne le template de la page d'inscription à un stage
    """
    persForm=PersonForm()
    autorForm=AutorStage_MineurForm()
    lieuForm=LieuForm()

    if persForm.validate_on_submit() & autorForm.validate_on_submit() & lieuForm.validate_on_submit():

        id_lieu = insert_lieu(lieuForm)
        id_pers, existing = insert_personne(persForm, id_lieu)

        if (existing):
            return redirect(url_for('other_connexion'))

        if not est_majeur(str(persForm.dateNPers.data)):
            return redirect(url_for('stage_inscription_parental', id_enfant = id_pers, ecole = str(persForm.ecole.data), niveau = int(persForm.niveau.data)))
        return redirect(url_for('stage_inscription_compte', id_pers = id_pers, ecole = str(persForm.ecole.data), niveau = int(persForm.niveau.data)))
    else:
        return render_template("stage/stage_inscription_basic.html",
                                persForm=persForm,
                                autorForm=autorForm,
                                lieuForm=lieuForm)

@app.route("/stage/inscription/compte", methods = ["GET", "POST"])
def stage_inscription_compte():

    userForm = CreateAccountForm()

    if userForm.validate_on_submit():
        mdpError = False
        userError = False

        if (str(userForm.mdp.data) != str(userForm.mdpConfirm.data)):
            mdpError = True

        if not try_username(str(userForm.username.data)):
            userError = True

        if userError or mdpError:
            print("ERRORS IN THE FORMS")
            return render_template("stage/stage_inscription_compte.html" ,
                                    userForm = userForm,
                                    userError = userError,
                                    mdpError = mdpError)

        insert_user(userForm, request.args.get('ecole', type=str), request.args.get('niveau', type=int), request.args.get('id_pers', 1, type=int))

        #TODO insert instruments joués
        print("REDIRECTING TO MEDS")

        return redirect(url_for('stage_inscription_autorisationMedicale'))
    else:
        return render_template("stage/stage_inscription_compte.html" ,
                                userForm = userForm,
                                userError = False,
                                mdpError = False)

@app.route("/stage/inscription/autorisation_parental", methods = ["GET", "POST"])
def stage_inscription_parental():
    """

    :return: Retourne le template de la page d'inscription à un stage
    """

    print("GENRATING FORMS")
    respLegForm=RespLegalForm()
    lieuForm=LieuForm()
    print("FORMS GENERATED")

    print(respLegForm.validate_on_submit())
    print(lieuForm.validate_on_submit())

    if respLegForm.validate_on_submit() & lieuForm.validate_on_submit():

        if not est_majeur(str(respLegForm.dateNPers.data)):
            return render_template("stage/stage_inscription_parental.html",
                                    respLegForm=respLegForm,
                                    lieuForm=lieuForm,
                                    ageError=True)

        print("FORMS VALIDATED")
        print("INSERTIONS")

        insert_lieu(lieuForm)
        insert_resp(respLegForm, lieuForm, request.args.get('id_enfant', type=int))
        print("REDIRECTION TO MEDICAL")
        return redirect(url_for('stage_inscription_compte', id_pers = request.args.get('id_enfant', type=int), ecole = request.args.get("ecole", type=str), niveau = request.args.get("niveau", type=int)))
    else:
        print("REDIRECTION TO EMPTY")
        return render_template("stage/stage_inscription_parental.html",
                                respLegForm=respLegForm,
                                lieuForm=lieuForm,
                                ageError=False)

@app.route("/stage/partitions/")
# @roles_required("STAGIAIRE")
def stage_partitions():
    """

    :return: Retourne le template de la page des partitions des musiques des stages
    """
    niveauForm = NiveauForm()
    return render_template("stage/stage_partitions.html", niveauForm = niveauForm)

@app.route("/stage/souvenirs/")
# @roles_required("STAGIAIRE")
def stage_souvenirs():
    """

    :return: Retourne le template de la page des souvenirs de stages
    """
    souvForm=SouvenirsForm()
    return render_template("stage/stage_souvenirs.html",
                            souvForm=souvForm)

@app.route("/stage/inscription/autorisationMedicale/", methods = ["GET", "POST"])
def stage_inscription_autorisationMedicale():
    """

    :return: Retourne le template de la page d'autorisation médicale pour un stage
    """
    form=AutorMedicForm()

    if form.validate_on_submit():
        #add bd
        return redirect(url_for('stage_inscription_valide'))
    return render_template("stage/stage_inscription_autorisationMedicale.html",
                            form=form)

@app.route("/stage/inscription/valide", methods = ["GET", "POST"])
def stage_inscription_valide():
    """

    :return: Retourne le template de la page de prise en compte de demande de stage
    """
    return render_template("stage/stage_inscription_valide.html")

@app.route("/stage/programmes/")
def stage_programmes():
    """

    :return: Retourne le template de la page des programmes de stages
    """
    return render_template("stage/stage_programmes.html")

@app.route("/stage/projetPeda/")
def stage_projetPeda():
    """

    :return:  Retourne le template de la page du projet pédagogique des stages
    """
    return render_template("stage/stage_projetPeda.html")

@app.route("/stage/concerts/")
def stage_concerts():
    """

    :return: Retourne le template de la page des concerts de stages
    """
    return render_template("stage/stage_concerts.html")

liste=[]
liste.append(["Le Quatuor a un nouveau site Web","22/12/2018","Olivier Roussillat","presentation-quatuor-1","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
liste.append(["Le Groupe 2A11b a fait le meilleur site web","23/12/2018","Sophie Anglade","presentation-quatuor-2","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
liste.append(["Car c'est notre projet!","24/12/2018","Adrien Foucault","presentation-quatuor-3","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico.Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."])
liste.append(["Un nouveau départ","12/01/2018","Michael Abid","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
liste.append(["Deux nouveaux départs","13/01/2018","Michael Abid","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
liste.append(["Trois nouveaux départs","14/01/2018","Alexis Chauvette","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
liste.append(["Quatre nouveaux départs","12/01/2018","Michael Abid","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
liste.append(["Cinq nouveaux départs","13/01/2018","Michael Abid","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
liste.append(["Six nouveaux départs","14/01/2018","Alexis Chauvette","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])

@app.route("/stage/presse/actu/")
def stage_presse_actu():
    """

    :return: Retourne le template correspondant a la page des articles de presse du stage actuelle
    """
    return render_template("stage/stage_presse_actu.html",liste=liste)

@app.route("/stage/presentation/<int:id>")
def stage_presentation_stage(id):
        """

        :return: Retourne le template correspondant a la description d'un stage
        """
        stage = get_stages(id = id);

        return render_template("stage/presentationStage.html", stage=stage)


@app.route("/stage/presse/all/<int:id>")
def stage_presse_all(id):
    """

    :return: Retourne le template correspondant a la page de touts les articles de presse en rapport avec le stage
    """
    ok=False
    listetrois=[]
    listetrois.append(liste[0])
    listetrois.append(liste[1])
    listetrois.append(liste[2])
    glistR=[]
    listeR=[]
    cpt=-1
    for elem in liste:
        cpt+=1
        listeR.append(elem)
        if cpt==5:
            cpt=0
            glistR.append(listeR)
            listeR=[]
    if listeR:
        glistR.append(listeR)
    print(listeR)
    page=[]
    try:
        page=glistR[id]

    except Exception as e:
        page=glistR[0]

    if len(glistR)>1:
        ok=True


    return render_template("stage/stage_presse_all.html",liste=page,caroussel=listetrois,id=id,ok=ok)

@app.route("/stage/presse/article/<nomarticle>")
def stage_presse(nomarticle):


    """
    :id: L'id de l'article de presse
    :return: Retourne le template correspondant a la page d'un article du stage
    """
    article=None
    for elem in liste:
        if elem[0]==nomarticle:
            article=elem
    if article==None:
            return render_template("other/page_404.html")
    return render_template("stage/stage_presse.html",article=article)

@app.route("/stage/repertoire/")
def stage_repertoire():
    """

    :return: Retourne le template de la page du repertoire musical des stages
    """
    return render_template("stage/stage_repertoire")

@app.route("/stage/paiement/")
def stage_paiement():
    """

    :return: Retourne le template de la page de paiement de stage
    """
    return render_template("stage/stage_paiement.html")

@app.route("/stage/recettes/")
# @roles_required("STAGIAIRE")
def stage_recettes():
    """

    :return: Retourne le template de la page des recettes
    """
    return render_template("stage/stage_recettes.html")
