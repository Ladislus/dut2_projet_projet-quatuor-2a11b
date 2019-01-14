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


liste=[]
liste.append(["Le Quatuor a un nouveau site Web","22/12/2018","Olivier Roussillat","presentation-quatuor-1","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
liste.append(["Le Groupe 2A11b a fait le meilleur site web","23/12/2018","Sophie Anglade","presentation-quatuor-2","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])
liste.append(["Car c'est notre projet!","24/12/2018","Andrien Foucault","presentation-quatuor-3","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine teste dico."])

@app.route("/quatuor/presse/all")
def quatuor_presse_all():
    """

    :return: Retourne le template correspondant a la page de touts les articles de presse en rapport avec le quatuor
    """
    return render_template("quatuor_presse_all.html",liste=liste)


@app.route("/quatuor/presse/article/<nomarticle>")
def quatuor_presse(nomarticle):
    article=None
    for elem in liste:
        if elem[0]==nomarticle:
            article=elem

    """
    :id: L'id de l'article de presse
    :return: Retourne le template correspondant a la page d'un artciel du quautor
    """
    if article==None:
            return render_template("page_404.html")
    return render_template("quatuor_presse.html",article=article)
