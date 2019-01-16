from .app import db, app
import click

@app.cli.command()
def init():
    """
    Commande initialisant la base de donnée
    """
    db.create_all()
