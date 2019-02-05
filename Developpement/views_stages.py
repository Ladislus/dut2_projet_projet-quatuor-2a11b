from .views import *
from .forms import *
@app.route("/stage/presentation/")
def stage_presentation():
    """

    :return: Retourne le template de la page de presentation de stage
    """
    return render_template("stage/stage_presentation.html")

@app.route("/stage/inscription/")
def stage_inscription():
    """

    :return: Retourne le template de la page d'inscription à un stage
    """
    persForm=PersonForm()
    respLegForm=RespLegalForm()
    autorSta_mineurForm=AutorStage_MineurForm()
    lieuForm=LieuForm()
    return render_template("stage/stage_inscription.html",
                            persForm=persForm,
                            respLegForm=respLegForm,
                            autorSta_mineurForm=autorSta_mineurForm,
                            lieuForm=lieuForm)

@app.route("/stage/inscription/autorisationMedicale/")
def stage_inscription_autorisationMedicale():
    """

    :return: Retourne le template de la page d'autorisation médicale pour un stage
    """
    form=AutorMedForm()
    return render_template("stage/stage_inscription_autorisationMedicale.html",form=form)

@app.route("/stage/inscription/valide")
def stage_inscription_valide():
    """

    :return: Retourne le template de la page de prise en compte de demande de stage
    """
    return render_template("stage/stage_inscription_valide.html")

@app.route("/stage/programmes/")
def stage_programmes():
    """

    :return: Retourne le template de la page des programmes de stages
    """
    return render_template("stage/stage_programmes.html")

@app.route("/stage/projetPeda/")
def stage_projetPeda():
    """

    :return:  Retourne le template de la page du projet pédagogique des stages
    """
    return render_template("stage/stage_projetPeda.html")

@app.route("/stage/concerts/")
def stage_concerts():
    """

    :return: Retourne le template de la page des concerts de stages
    """
    return render_template("stage/stage_concerts.html")

@app.route("/stage/presse/")
def stage_presse():
    """

    :return: Retourne le template de la page de la presse liée au stages
    """
    return render_template("stage/stage_presse.html")

@app.route("/stage/repertoire/")
def stage_repertoire():
    """

    :return: Retourne le template de la page du repertoire musical des stages
    """
    return render_template("stage/stage_repertoire")

@app.route("/stage/paiement/")
def stage_paiement():
    """

    :return: Retourne le template de la page de paiement de stage
    """
    return render_template("stage/stage_paiement.html")

@app.route("/stage/partitions/")
def stage_partitions():
    """

    :return: Retourne le template de la page des partitions des musiques des stages
    """
    return render_template("stage/stage_partitions.html")

@app.route("/stage/partitions/niveau1/")
def stage_partitions_niveau1():
    """

    :return: Retourne le template de la page des partitions des musiques des stages de niveau 1
    """
    return render_template("stage/stage_partitions_niveau1.html")


@app.route("/stage/partitions/niveau2/")
def stage_partitions_niveau2():
    """

    :return: Retourne le template de la page des partitions des musiques des stages de niveau 2
    """
    return render_template("stage/stage/stage_partitions_niveau2.html")


@app.route("/stage/partitions/niveau3/")
def stage_partitions_niveau3():
    """

    :return: Retourne le template de la page des partitions des musiques des stages de niveau 3
    """
    return render_template("stage/stage_partitions_niveau3.html")

@app.route("/stage/souvenirs/")
def stage_souvenirs():
    """

    :return: Retourne le template de la page des souvenirs de stages
    """
    return render_template("stage/stage_souvenirs.html")

@app.route("/stage/recettes/<int:id>")
def stage_recettes_unitaire():
    """

    :return: Retourne le template de la page de la recette sur laquelle on a cliqué
    """
    return render_template("stage/stage_recettes_unitaire.html")

@app.route("/stage/recettes/")
def stage_recettes():
    """

    :return: Retourne le template de la page des recettes
    """
    return render_template("stage/stage_recettes.html")
