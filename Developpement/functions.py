from .app import login_manager, app, db

import click
from hashlib import sha512
from datetime import datetime, timedelta

# def insert_personne(form):
#     added_user = Personne(nomPers = form.nomPers.data, prenomPers = form.prenomPers.data, mailPers = form.mailPers.data, telPersUn = form.tel1Pers.data, dateNPers = form.dateNPers.data)
#     db.session.add(added_user)
#     db.commit()

@app.cli.command()
def session_commit():
    """
    Commit la session courante
    """
    db.session.commit()

def crypt(password):
    """
    Crypte le parametre "password" (String) avec le SHA512
    """
    crypter = sha512() #créer un objet SHA512
    crypter.update(password.encode()) #crypte str(password) grâce à l'objet crypter
    return crypter.hexigest() #return le password crypter en base16

@app.cli.command()
def init_db(filename = None):
    """
    Initialise la base de donnée
    """
    db.create_all()

def est_majeur(str_date):
    """
    Renvoie un boolean si l'écart entre str_date et la date actuelle est supérieur à 18 ans
    """
    date = datetime.strptime(str_date, '%Y-%m-%d') #Converti la date str(YYYY-MM-DD) en objet datetime
    gap = datetime.now() - date #gap contient la différence de temp entre str_date et la date actuelle
    return gap.total_seconds() > (60 * 60 * 24 * 365 * 18) #return si gap > 18 ans (en secondes)

@login_manager.user_loader
def load_user(username):
    return Utilisateur.query.get(username)
