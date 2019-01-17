from .views import *
@app.route("/other/liens/")
def other_liens():
    """

    :return: Retourne le template de la page dédiée aux liens utiles
    """
    return render_template("other/page_liens.html")

@app.route("/other/connexion/")
def other_connexion():
    """

    :return: Retourne le templates de la page de connexion

    """
    return render_template("other/connexion.html")

@app.route("/other/deconnexion/")
def other_deconnexion():
    """

    :return: Retourne le template de la page de deconnexion
    """
    return render_template("other/deconnexion.html")

@app.route("/other/mdpOublie/")
def other_mdpOublie():
    """

    :return: Retourne le template de la page d'oublie de mot de passe
    """
    return render_template("other/mdpOublie.html")

@app.route("/other/concerts/")
def quatuor_concerts():
    """

    :return: Retourne le template correspondant a la page des concerts
    """
    return render_template("other/concerts.html")


#NE PAS PRENDRE EN COMPTE
@app.route("/other/test/")
def other_test():
    """

    :return: Retourne le template de la page de test
    """
    return render_template("other/testjs.html")
