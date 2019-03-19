from .views import *
from .forms import *

from flask_login import login_user;

@app.route("/other/liens/")
def other_liens():
    """

    :return: Retourne le template de la page dédiée aux liens utiles
    """
    return render_template("other/page_liens.html")

@app.route("/other/inscription")
def other_inscription():
    """
    """
    return render_template("other/inscription.html")

@app.route("/other/connexion/")
def other_connexion():
    """

    :return: Retourne le templates de la page de connexion

    """
    connectForm=ConnectForm()
    if not connectForm.is_submitted():
        connectForm.next.data = request.args.get("next")
    elif connectForm.validate_on_submit():
        user = connectForm.get_authentificated_user()
        if user:
            login_user(user)
            next = connectForm.next.data or url_for("home")
            return redirect(next)
    return render_template("other/connexion.html",
                            connectForm=connectForm)

@app.route("/other/deconnexion/")
def other_deconnexion():
    """

    :return: Retourne le template de la page de deconnexion
    """
    user_logout()
    return redirect("home")

@app.route("/other/mdpOubli/")
def other_mdpOublie():
    """

    :return: Retourne le template de la page d'oublie de mot de passe
    """
    oubliForm=OubliMdpForm()

    return render_template("other/mbpOubli.html",oubliForm=oubliForm)

@app.route("/other/concerts/")
def quatuor_concerts():
    """

    :return: Retourne le template correspondant a la page des concerts
    """
    return render_template("other/concerts.html")


@app.errorhandler(404)
def page_not_found(e):
    """

    :return: Retourne le template correspondant a la page erreur 404
    """
    return render_template('other/page_404.html'),404

#NE PAS PRENDRE EN COMPTE
@app.route("/other/test/")
def other_test():
    """

    :return: Retourne le template de la page de test
    """
    form=PersonForm()
    form2=RespLegalForm()
    form3=AutorStage_MineurForm()
    return render_template("other/testjs.html", form=form, form2=form2, form3=form3)
