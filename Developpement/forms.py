from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired

class PersonForm(FlaskForm):
    id          = HiddenField('idPers')
    nomPers     = StringField('Nom', validators[DataRequired()])
    prenomPers  = StringField('Prénom', validators[DataRequired()])
    mailPers    = StringField('Adresse Mail', validators[DataRequired()])
    tel1Pers    = StringField('Téléphone principal', validators[DataRequired()])
    tel2Pers    = StringField('Téléphone optionnel')
    dateNPers   = DateField('Date de naissance', validators[DataRequired()])
    idTuteur    = HiddenField('idTuteur')

    idLieu      = StringField('Adresse', validators[DataRequired()])

class UserForm(FlaskForm):
    idUt          = HiddenField('idUt')
    ecoleUt     = StringField('Ecole de Musique')
    nivUt       = IntegerField('Niveau')
    usernameUt  = StringField('Nom d\'utlisateur', validators[DataRequired()])
    mdpUt       = PasswordField('Mot de Passe', validators[DataRequired()])

    idPers      = HiddenField('personneLiee ?')

class StageForm(FlaskForm):
    idSt        = HiddenField('idSt')
    idRep       = HiddenField('idRep')
    intituleSt  = StringField('Intitule du stage', validators[DataRequired()])
    nbPlaceSt   = IntegerField('Nombre de places dispos', validators[DataRequired()])
    dateDebSt   = DateField('Date de début du stage', validators[DataRequired()])
    dateFinSt   = DateField('Date de fin du stage', validators[DataRequired()])
    tenueSt     = StringField('Tenue exigée pour le concert du stage')
    prixSt      = FloatField('Prix du stage')
    descStage   = TextField('Description du stage', validators[DataRequired()])
    nivRequisSt = IntegerField('Niveau minimum pour intégrer le stage')

    idLieu      = StringField('Adresse', validators[DataRequired()])

class ArticleForm(FlaskForm):
    idArt       = HiddenField('idSt')
    titreArt    = StringField('Titre de l\'article')
    contenuArt  = TextField('Description article')

    idUt        = HiddenField('Auteur de l\'article')

class ComForm(FlaskForm):
    idCom       = HiddenField('idCom')
    contenuCom  = TextField('Contenu commentaire')

    idUt        = HiddenField('Auteur du commentaire')
