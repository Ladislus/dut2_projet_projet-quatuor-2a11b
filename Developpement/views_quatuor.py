from .views import *
from .model_quatuor import *

@app.route("/")
def home():
    """

    :return: Retourne le template correspondant a la page de la presentation du quatuor
    """
    return render_template("quatuor_presentation.html")

@app.route("/quatuor/presentation/")
def quatuor_presentation():
    """

    :return: Retourne le template correspondant a la page de la presentation du quatuor
    """
    return render_template("quatuor_presentation.html")

@app.route("/quatuor/repertoire/")
def quatuor_repertoire():
    """

    :return: Retourne le template correspondant a la page du repertoire du quatuor
    """
    return render_template("quatuor_repertoire.html")

@app.route("/quatuor/extrait/")
def quatuor_extrait():
    """

    :return: Retourne le template correspondant a la page des extraits du quatuor
    """
    return render_template("quatuor_extrait.html")

@app.route("/quatuor/concerts/")
def quatuor_concerts():
    """

    :return: Retourne le template correspondant a la page des concerts du quatuor
    """
    return render_template("quatuor_concerts.html")


@app.route("/quatuor/presse/actu")
def quatuor_presse_actu():
    """

    :return: Retourne le template correspondant a la page des articles de presse du quatuor actuelle
    """
    return render_template("quatuor_presse_actu.html")


@app.route("/quatuor/presse/all")
def quatuor_presse_all():
    """

    :return: Retourne le template correspondant a la page de touts les articles de presse en rapport avec le quatuor
    """
    return render_template("quatuor_presse_all.html")


@app.route("/quatuor/presse/<int:id>")
def quatuor_presse(id):
    """
    :id: L'id de l'article de presse
    :return: Retourne le template correspondant a la page d'un artciel du quautor
    """
    return render_template("quatuor_presse.html",id=id)
