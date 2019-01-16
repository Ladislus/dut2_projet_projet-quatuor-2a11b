from .views import *
@app.route("/other/liens/")
def contact_liens():
    """

    :return: Retourne le template de la page dédiée aux liens utiles
    """
    return render_template("other/page_liens.html")

@app.route("/other/connexion/")
def contact_connexion():
    """

    :return: Retourne le template de la page de connexion
    """
    return render_template("other/connexion.html")

@app.route("/other/mdpOublie/")
def contact_mdpOublie():
    """

    :return: Retourne le template de la page d'oublie de mot de passe
    """
    return render_template("mdpOublie.html")
