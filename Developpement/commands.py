from .app import db, app
import click

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    '''Creates the tables and populates them with data.'''

    # creation de toutes les tables
    db.create_all()
