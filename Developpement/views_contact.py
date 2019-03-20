from .views import *
import datetime



@app.route("/contact/administratif/")
def contact_administratif():
    """

    :return: Retourne le template de la partie administrative du contact
    """

    user_contactForm = User_ContactForm()
    return render_template("contact/contact_administratif.html",user_contactForm=user_contactForm)

@app.route("/contact/mentionsLegales/")
def contact_mentionsLegales():
    """

    :return: Retourne le template des mentions légales du site
    """
    return render_template("contact/contact_mentionsLegales.html")

@app.route("/contact/renseignements/")
def contact_renseignements():
    """

    :return: Retourne le template des renseignements sur le site
    """
    return render_template("contact/contact_renseignements.html")

@app.route("/contact/ficheTechnique/")
def contact_ficheTechnique():
    """

    :return: Retourne le template de la fiche tchnique des concerts
    """
    return render_template("contact/contact_ficheTechnique.html")

@app.route("/contact/plaquette/")
def contact_plaquette():
    """

    :return: Retourne le template de la plaquette actuelle
    """
    now = datetime.datetime.now()
    ListePlaquette={}
    for i in range(now.year,2017,-1):
        i = str(i)
        ListePlaquette[i]=[]
        ListePlaquette[i].append("PLAQUETTE_STAGE_-_"+str(i)+"_-_Niveau_1_Adultes.pdf")
        ListePlaquette[i].append("PLAQUETTE_STAGE_-_"+str(i)+"_-_Niveau_1.pdf")
        ListePlaquette[i].append("PLAQUETTE_STAGE_-_"+str(i)+"_-_Niveau_2.pdf")
    return render_template("contact/contact_plaquette.html",ListePlaquette=ListePlaquette)
