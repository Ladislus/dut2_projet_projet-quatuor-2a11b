from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, DateField, IntegerField, FloatField, FieldList, FormField
from wtforms.validators import DataRequired

class PersonForm(FlaskForm):
    nomPers         = StringField('Nom', validators[DataRequired()])
    prenomPers      = StringField('Prénom', validators[DataRequired()])
    dateNPers       = DateField('Date de naissance', validators[DataRequired()])
    tel1Pers        = StringField('Téléphone principal', validators[DataRequired()])
    mailPers        = StringField('Adresse Mail', validators[DataRequired()])
    clarJouees      = FieldList(FormField(StringField('Clarinette jouée')))
    niveau          = IntegerField('Année d\'experience')
    ecole           = StringField('Ecole')
    typePratique    = StringField('Type de pratique')

class RespLegalForm(FlaskForm):
    nomResp         = StringField('Nom du Responsable')
    prenomResp      = StringField('Prénom du Responsable')
    adrResp         = StringField('Adresse du Responsable')
    CPResp          = StringField('Code Postal du Responsable')
    villeResp       = StringField('Ville du Responsable')
    telPers         = StringField('Téléphone personnel')
    telTrav         = StringField('Téléphone travail')
    mailPers        = StringField('Adresse Mail', validators[DataRequired()])
    mailTrav        = StringField('Adresse Mail', validators[DataRequired()])

# class UserForm(FlaskForm):
#     idUt        = HiddenField('idUt')
#     ecoleUt     = StringField('Ecole de Musique')
#     nivUt       = IntegerField('Niveau')
#     usernameUt  = StringField('Nom d\'utlisateur', validators[DataRequired()])
#     mdpUt       = PasswordField('Mot de Passe', validators[DataRequired()])
#
#     idPers      = HiddenField('personneLiee ?')
#
# class StageForm(FlaskForm):
#     idSt        = HiddenField('idSt')
#     idRep       = HiddenField('idRep')
#     intituleSt  = StringField('Intitule du stage', validators[DataRequired()])
#     nbPlaceSt   = IntegerField('Nombre de places dispos', validators[DataRequired()])
#     dateDebSt   = DateField('Date de début du stage', validators[DataRequired()])
#     dateFinSt   = DateField('Date de fin du stage', validators[DataRequired()])
#     tenueSt     = StringField('Tenue exigée pour le concert du stage')
#     prixSt      = FloatField('Prix du stage')
#     descStage   = TextField('Description du stage', validators[DataRequired()])
#     nivRequisSt = IntegerField('Niveau minimum pour intégrer le stage')
#
#     idLieu      = StringField('Adresse', validators[DataRequired()])
