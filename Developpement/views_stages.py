from .views import *
from .forms import *
@app.route("/stage/<int:id>")
def stage_Id(id):
    a = get_stage(id)
    return render_template("stage.html",
            title=a.intituleSt)
        

@app.route("/stage/presentation/")
def stage_presentation():
    """

    :return: Retourne le template de la page de presentation de stage
    """
    return render_template("stage/stage_presentation.html")

@app.route("/stage/inscription/")
def stage_inscription():
    """

    :return: Retourne le template de la page d'inscription à un stage
    """
    persForm=PersonForm()
    respLegForm=RespLegalForm()
    autorSta_mineurForm=AutorStage_MineurForm()
    lieuForm=LieuForm()
    return render_template("stage/stage_inscription.html",
                            persForm=persForm,
                            respLegForm=respLegForm,
                            autorSta_mineurForm=autorSta_mineurForm,
                            lieuForm=lieuForm)

@app.route("/stage/inscription/autorisationMedicale/")
def stage_inscription_autorisationMedicale():
    """

    :return: Retourne le template de la page d'autorisation médicale pour un stage
    """
    form=AutorMedForm()
    return render_template("stage/stage_inscription_autorisationMedicale.html",form=form)

@app.route("/stage/inscription/valide")
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
liste.append(["Car c'est notre projet!","24/12/2018","Andrien Foucault","presentation-quatuor-3","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
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

@app.route("/stage/partitions/")
def stage_partitions():
    """

    :return: Retourne le template de la page des partitions des musiques des stages
    """
    return render_template("stage/stage_partitions.html")

@app.route("/stage/partitions/niveau1/")
def stage_partitions_niveau1():
    """

    :return: Retourne le template de la page des partitions des musiques des stages de niveau 1
    """
    return render_template("stage/stage_partitions_niveau1.html")


@app.route("/stage/partitions/niveau2/")
def stage_partitions_niveau2():
    """

    :return: Retourne le template de la page des partitions des musiques des stages de niveau 2
    """
    return render_template("stage/stage/stage_partitions_niveau2.html")


@app.route("/stage/partitions/niveau3/")
def stage_partitions_niveau3():
    """

    :return: Retourne le template de la page des partitions des musiques des stages de niveau 3
    """
    return render_template("stage/stage_partitions_niveau3.html")

@app.route("/stage/souvenirs/")
def stage_souvenirs():
    """

    :return: Retourne le template de la page des souvenirs de stages
    """
    return render_template("stage/stage_souvenirs.html")

@app.route("/stage/recettes/<int:id>")
def stage_recettes_unitaire():
    """

    :return: Retourne le template de la page de la recette sur laquelle on a cliqué
    """
    return render_template("stage/stage_recettes_unitaire.html")

@app.route("/stage/recettes/")
def stage_recettes():
    """

    :return: Retourne le template de la page des recettes
    """
    return render_template("stage/stage_recettes.html")
