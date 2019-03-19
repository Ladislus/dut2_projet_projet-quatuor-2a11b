from .app import db, app
from .models import Role

from sqlalchemy.exc import IntegrityError

import click

@app.cli.command()
def init():
    """
    Commande initialisant la base de donnée
    """
    db.create_all()

@app.cli.command()
@click.argument('nom')
def new_role(nom):
    """
    créer un nouveau role
    """
    r = Role(nomRole = nom)
    db.session.add(r)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        print("\n\tRole déjà existant !\n")
