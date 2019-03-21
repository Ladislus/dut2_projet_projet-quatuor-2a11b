from .views import *
from .forms import *
from .models import *



from flask_login import login_user, logout_user, current_user;

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

@app.route("/other/connexion/", methods = ["GET", "POST"])
def other_connexion():
    """

    :return: Retourne le templates de la page de connexion

    """
    connectForm=ConnectForm()

    if connectForm.validate_on_submit():

        user = connectForm.get_user()
        print("USER FROM FORM : " + str(user))

        if user is None:
            print("ERROR DURING LOGGING")
            return render_template("other/connexion.html", connectForm=connectForm, errorLogin=True)

        login_user(user)
        print("SUCCESSFULLY LOGGED IN")
        return redirect(url_for("home"))

    return render_template("other/connexion.html", connectForm=connectForm)



@app.route("/other/deconnexion/")
def other_deconnexion():
    """

    :return: Retourne le template de la page de deconnexion
    """
    logout_user()
    return redirect(url_for("home"))

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


@app.route("/other/profil")
def profile():
    """

    :return: Retourne le template correspondant au profil de l'utilisateur
    """
    a=get_user(current_user.usernameUt)
    return render_template("other/profil.html", utilisateur=a)
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
