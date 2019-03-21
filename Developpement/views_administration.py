from .views import *

@app.route("/administration/")
@roles_required('ADMIN')
def administration():
    """

    :return: Retourne le template de la page d'administration
    """
    return render_template("administration/administration.html")

@app.route("/administration/mailing/")
@roles_required('ADMIN')
def administration_mailing():
    """

    :return: Retourne le template de la page de mailing
    """


    admin_contactForm = Admin_ContactForm()
    return render_template("administration/administration_mailing.html",
                            admin_contactForm=admin_contactForm)

@app.route("/administration/gestionStages/", methods = ["GET", "POST"])
@roles_required('ADMIN')
def administration_gestionStages():
    """

    :return: Retourne le template de la page de gestion des stages
    """
    return render_template("administration/administration_gestionStages.html", dico_stage=get_stages())

@app.route("/administration/modifierStage/")
@roles_required('ADMIN')
def administration_modifierStage():
    """

    :return: Retourne le template de la page de gestion des stages
    """
    creaStageForm=StageForm()
    lieuForm=LieuForm()
    return render_template("administration/administration_modifierStage.html",creaStageForm=creaStageForm,
    lieuForm=lieuForm)

@app.route("/administration/gestionFichiers/")
@roles_required('ADMIN')
def administration_gestionFichiers():
    """

    :return: Retourne le template de la page de gestion des fichiers présents sur le site
    """
    return render_template("administration/administration_gestionFichiers.html")

@app.route("/administration/gestionFichiers/images/")
@roles_required('ADMIN')
def administration_gestionFichiers_images():
    """

    :return: Retourne le template de la page de gestion des images
    """
    return render_template("administration/administration_gestionFichiers_images.html")



@app.route("/administration/gestionFichiers/images/modification/")
@roles_required('ADMIN')
def administration_gestionFichiers_images_modification():
    """

    :return: Retourne le template de la page de modification d'une image qui sera dans une popup
    """
    return render_template("administration/administration_gestionFichiers_images_modification.html")

@app.route("/administration/gestionFichiers/videos/")
@roles_required('ADMIN')
def administration_gestionFichiers_videos():
    """

    :return: Retourne le template de la page de gestion des videos
    """
    dico={}
    dico['Quatuor']=[]
    dico['Quatuor'].append(["Video 1","MP4",url_for('static',filename='video/video1.mp4'),url_for('static',filename='video/video1.mp4')])
    dico['Stage']=[]
    dico['Stage'].append(["Video 2","MP4",url_for('static',filename='video/video2.mp4'),url_for('static',filename='video/video2.mp4')])
    # dico['Stage'].append(["Video 5","MP4","{{ url_for('static',filename='img/entree2.jpg') }}"])
    dico['Concerts']=[]
    dico['Concerts'].append(["Video 3","MP4",url_for('static',filename='video/video3.mp4'),url_for('static',filename='video/video3.mp4')])
    dico['Concerts'].append(["Video 4","MP4",url_for('static',filename='video/video4.mp4'),url_for('static',filename='video/video4.mp4')])
    dico['Clarinette']=[]
    dico['Clarinette'].append(["Video 5","WEBM",url_for('static',filename='video/video5.webm'),url_for('static',filename='video/video5.webm')])
    # dico['Clarinette'].append(["Video 1","MP4","{{ url_for('static',filename='img/entree2.jpg') }}"])
    return render_template("administration/administration_gestionFichiers_videos.html",dico_videos=dico)


@app.route("/administration/gestionFichiers/videos/modification/")
@roles_required('ADMIN')
def administration_gestionFichiers_videos_modification():
    """

    :return: Retourne le template de la page de modification d'une video qui sera dans une popup
    """
    return render_template("administration/administration_gestionFichiers_videos_modification.html")

@app.route("/administration/gestionFichiers/articles/")
@roles_required('ADMIN')
def administration_gestionFichiers_aticles():
    """

    :return: Retourne le template de la page de gestion des textes
    """
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


    return render_template("administration/administration_gestionFichiers_articles.html",dico_articles=liste)

@app.route("/administration/gestionFichiers/textes/modification")
@roles_required('ADMIN')
def administration_gestionFichiers_textes_modification():
    """

    :return: Retourne le template de la page de modification d'un texte qui sera dans une popup
    """
    return render_template("administration/administration_gestionFichiers_articles_modification.html")

@app.route("/administration/gestionStagiaires/")
@roles_required('ADMIN')
def administration_gestionStagiaires():
    """

    :return: Retourne le template de la page de gestion des stagiaires
    """
    dico={}
    dico['2018']=[]#Nom Prenom age niveau mail role
    dico['2018'].append(["Abid","Michael","19","1","michael.abid@outlook.fr","user"])
    dico['2018'].append(["Foucault","Adrien","18","2","adrien.foucault@outlook.fr","user"])
    dico['2017']=[]#Nom Prenom age niveau mail role
    dico['2017'].append(["Walcak","Ladislas","19","3","ladislas.walcak@outlook.fr","user"])
    dico['2017'].append(["Demarest","Liam","19","1","liam.demarest@outlook.fr","user"])
    return render_template("administration/administration_gestionStagiaires.html",dico_stagiaire=dico)

@app.route("/administration/modifierStagiaire/")
@roles_required('ADMIN')
def administration_gestionStagiaires_Stagiaire():
    """

    :return: Retourne le template de la page de gestion d'un stagiaire
    """
    modifStagiaire=PersonForm()
    return render_template("administration/administration_gestionStagiaires_stagiaire.html",modifStagiaire=modifStagiaire)

@app.route("/administration/creerStage/", methods = ["GET", "POST"])
# @roles_required("ADMIN")
def administration_creerStage():
    """

    :return: Retourne le template de la page de creation de stage
    """

    stageForm=StageForm()

    if stageForm.validate_on_submit():

        try:
            insert_stage(stageForm)
            print("NORMALEMENT LA REDIRECTION")
            return redirect(url_for('administration_gestionStages'))
        except ValueError:
            return render_template("administration/administration_creerStage.html",
                                    stageForm=stageForm,
                                    timeError=True,
                                    titleError=False)
        except NameError:
            return render_template("administration/administration_creerStage.html",
                                    stageForm=stageForm,
                                    timeError=False,
                                    titleError=True)



    else:
        return render_template("administration/administration_creerStage.html",
                                stageForm=stageForm,
                                timeError=False)
