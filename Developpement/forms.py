from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FieldList, FormField, IntegerField, TextField, FileField, PasswordField, HiddenField
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
    nomResp         = StringField('Nom du Responsable', validators[DataRequired()])
    prenomResp      = StringField('Prénom du Responsable', validators[DataRequired()])
    adrResp         = StringField('Adresse du Responsable', validators[DataRequired()])
    CPResp          = StringField('Code Postal du Responsable', validators[DataRequired()])
    villeResp       = StringField('Ville du Responsable', validators[DataRequired()])
    telPers         = StringField('Téléphone personnel', validators[DataRequired()])
    telTrav         = StringField('Téléphone travail')
    mailPers        = StringField('Adresse Mail Personnelle', validators[DataRequired()])
    mailTrav        = StringField('Adresse Mail de Travail')

class User_ContactForm(FlaskForm):
    objetMessage    = SelectField('Objet')
    contenuMessage  = TextField('Contenu message')
    pjMessage       = FieldList(FormField(FileField('Pièce-jointe')))

class AutorMedForm(FlaskForm):
    numContactUrg1  = StringField('Numero à contacter Urgence 1')
    numContactUrg2  = StringField('Numero à contacter Urgence 2')

class AutorStage_MineurForm(FlaskForm):
    autorAudioPrive = BooleanField('Autorisation utilisation audio en privé')
    autorAudioPub   = BooleanField('Autorisation utilisation audio sur le site quatuor')
    autorImag       = BooleanField('Autorisation utilisation image dans le cadre du stage')
    autorImagSite   = BooleanField('Autorisation utilisation image sur le site du quatuor')

class 

class LoginForm(FlaskForm):
    username        = StringField('Nom d\'utilisateur')
    mdp             = HiddenField('Mot de passe')
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
