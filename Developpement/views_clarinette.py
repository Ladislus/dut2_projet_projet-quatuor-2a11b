from .views import *

@app.route("/autourClarinette/historique/")
def clarinette_historique():
    """

    :return: Retourne le template de la partie historique de l'onglet "Autour de la clarinette"
    """
    return render_template("clarinette/clarinette_historique.html")

@app.route("/autourClarinette/informations/")
def clarinette_informations():
    """

    :return: Retourne le template des informations autour de la clarinette
    """
    return render_template("clarinette/clarinette_informations.html")

@app.route("/autourClarinette/datesConcerts/")
def clarinette_datesConcerts():
    """

    :return: Retourne le template des dates de concerts du quatuor
    """
    return render_template("clarinette/clarinette_datesConcerts.html")
