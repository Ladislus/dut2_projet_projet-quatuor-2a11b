from .views import *
from .model_quatuor import *

@app.route("/")
def home():
    """

    :return: Retourne le template correspondant à la page de la présentation du quatuor
    """
    return render_template("quatuor_presentation.html")

@app.route("/quatuor/presentation/")
def quatuor_presentation():
    """

    :return: Retourne le template correspondant à la page de la présentation du quatuor
    """
    return render_template("quatuor_presentation.html")

@app.route("/quatuor/repertoire/")
def quatuor_repertoire():
    """

    :return: Retourne le template correspondant à la page du répertoire du quatuor
    """
    return render_template("quatuor_repertoire.html")

@app.route("/quatuor/extrait/")
def quatuor_extrait():
    """

    :return: Retourne le template correspondant à la page des extraits du quatuor
    """
    return render_template("quatuor_extrait.html")

@app.route("/quatuor/concerts/")
def quatuor_concerts():
    """

    :return: Retourne le template correspondant à la page des concerts du quatuor
    """
    return render_template("quatuor_concerts.html")


@app.route("/quatuor/presse/")
def quatuor_presse():
    """

    :return: Retourne le template correspondant à la page des articles de presse du quatuor
    """
    return render_template("quatuor_presse.html")
