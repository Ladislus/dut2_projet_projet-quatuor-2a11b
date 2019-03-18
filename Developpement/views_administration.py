from .views import *
from .forms import *
@app.route("/administration")
def administration():
    """

    :return: Retourne le template de la page d'administration
    """
    return render_template("administration/administration.html")

@app.route("/administration/mailing/")
def administration_mailing():
    """

    :return: Retourne le template de la page de mailing
    """
    admin_contactForm = Admin_ContactForm()
    return render_template("administration/administration_mailing.html",
                            admin_contactForm=admin_contactForm)

@app.route("/administration/gestionStages/")
def administration_gestionStages():
    """

    :return: Retourne le template de la page de gestion des stages
    """
    dico={}
    dico['2018']=[]
    dico['2018'].append(["04","Repertoire 1","Stage d'été","1 rue Michel","28000","Chartres","30","01/01/2018","01/02/2018","costume","10.0€","zjhreuzhruz","Niveau 1"])
    dico['2018'].append(["03","Repertoire 2","Stage hiver","1 rue Michel","28000","Chartres","30","01/03/2018","01/04/2018","costume","15.0€","zjhreuzhruz","Niveau 2"])
    dico['2017']=[]
    dico['2017'].append(["02","Repertoire 3","Stage printemps","1 rue Michel","28000","Chartres","30","01/01/2017","01/02/2017","costume","25.0€","zjhreuzhruz","Niveau 1"])
    dico['2017'].append(["01","Repertoire 1","Stage automne","1 rue Michel","28000","Chartres","30","01/05/2017","01/06/2017","costume","20.0€","zjhreuzhruz","Niveau 3"])
    return render_template("administration/administration_gestionStages.html", dico_stage=dico)

@app.route("/administration/modifierStage/")
def administration_modifierStage():
    """

    :return: Retourne le template de la page de gestion des stages
    """
    creaStageForm=StageForm()
    lieuForm=LieuForm()
    return render_template("administration/administration_modifierStage.html",creaStageForm=creaStageForm,
    lieuForm=lieuForm)

@app.route("/administration/gestionFichiers/")
def administration_gestionFichiers():
    """

    :return: Retourne le template de la page de gestion des fichiers présents sur le site
    """
    return render_template("administration/administration_gestionFichiers.html")

@app.route("/administration/gestionFichiers/images/")
def administration_gestionFichiers_images():
    """

    :return: Retourne le template de la page de gestion des images
    """
    return render_template("administration/administration_gestionFichiers_images.html")



@app.route("/administration/gestionFichiers/images/modification/")
def administration_gestionFichiers_images_modification():
    """

    :return: Retourne le template de la page de modification d'une image qui sera dans une popup
    """
    return render_template("administration/administration_gestionFichiers_images_modification.html")

@app.route("/administration/gestionFichiers/videos/")
def administration_gestionFichiers_videos():
    """

    :return: Retourne le template de la page de gestion des videos
    """
    return render_template("administration/administration_gestionFichiers_videos.html")

@app.route("/administration/gestionFichiers/videos/modification/")

def administration_gestionFichiers_videos_modification():
    """

    :return: Retourne le template de la page de modification d'une video qui sera dans une popup
    """
    return render_template("administration/administration_gestionFichiers_videos_modification.html")

@app.route("/administration/gestionFichiers/textes/")
def administration_gestionFichiers_textes():
    """

    :return: Retourne le template de la page de gestion des textes
    """
    return render_template("administration/administration_gestionFichiers_textes.html")

@app.route("/administration/gestionFichiers/textes/modification")
def administration_gestionFichiers_textes_modification():
    """

    :return: Retourne le template de la page de modification d'un texte qui sera dans une popup
    """
    return render_template("administration/administration_gestionFichiers_textes_modification.html")

@app.route("/administration/gestionStagiaires/")
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
def administration_gestionStagiaires_Stagiaire():
    """

    :return: Retourne le template de la page de gestion d'un stagiaire
    """
    modifStagiaire=PersonForm()
    return render_template("administration/administration_gestionStagiaires_stagiaire.html",modifStagiaire=modifStagiaire)

@app.route("/administration/creerStage/")
def administration_creerStage():
    """

    :return: Retourne le template de la page de creation de stage
    """
    creaStageForm=StageForm()
    lieuForm=LieuForm()
    return render_template("administration/administration_creerStage.html",
                            creaStageForm=creaStageForm,
                            lieuForm=lieuForm)
