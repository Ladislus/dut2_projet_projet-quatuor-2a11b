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
    return render_template("administration/administration_gestionStages.html")

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

@app.route("/administration/gestionStagiaires/Stagiaire/")
def administration_gestionStagiaires_Stagiaire():
    """

    :return: Retourne le template de la page de gestion d'un stagiaire
    """
    return render_template("administration/administration_gestionStagiaires_stagiaire.html")

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
