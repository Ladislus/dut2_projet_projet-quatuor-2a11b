@app.route("/contact/administratif")
def contact_administratif():
    """

    :return: Retourne le template de la partie administrative du contact
    """
    return render_template("contact_administratif.html")

@app.route("/contact/mentionsLegales")
def contact_mentionsLegales():
    """

    :return: Retourne le template des mentions légales du site
    """
    return render_template("contact_mentionsLegales.html")

@app.route("/contact/renseignements")
def contact_renseignements():
    """

    :return: Retourne le template des renseignements sur le site
    """
    return render_template("contact_renseignements.html")

@app.route("/contact/ficheTechnique")
def contact_ficheTechnique():
    """

    :return: Retourne le template de la fiche tchnique des concerts
    """
    return render_template("contact_ficheTechnique.html")

@app.route("/contact/plaquette")
def contact_plaquette():
    """

    :return: Retourne le template de la plaquette actuelle
    """
    return render_template("contact_plaquette.html")

    @app.route("/contact/plaquette")

def contact_musical():
    """

    :return: Retourne le template des partenaires musicaux du groupe
    """
    return render_template("contact_plaquette.html")