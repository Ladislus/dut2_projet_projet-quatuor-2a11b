from .functions import crypt
from .getters import get_user
from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, FieldList, FileField, FloatField, FormField, HiddenField, IntegerField, PasswordField, SelectField, StringField, TextField
from wtforms.validators import DataRequired

class PersonForm(FlaskForm):
    nomPers         = StringField('Nom', validators=[DataRequired()])
    prenomPers      = StringField('Prénom', validators=[DataRequired()])
    dateNPers       = DateField('Date de naissance', validators=[DataRequired()])
    tel1Pers        = StringField('Téléphone principal', validators=[DataRequired()])
    mailPers        = StringField('Adresse Mail', validators=[DataRequired()])
    clarJouees      = FieldList(FormField(StringField('Clarinette jouée')), validators=[DataRequired()])
    niveau          = IntegerField('Année d\'experience', validators=[DataRequired()])
    ecole           = StringField('Ecole', validators=[DataRequired()])
    typePratique    = StringField('Type de pratique')

class RespLegalForm(FlaskForm):
    nomResp         = StringField('Nom du Responsable', validators=[DataRequired()])
    prenomResp      = StringField('Prénom du Responsable', validators=[DataRequired()])
    adrResp         = StringField('Adresse du Responsable', validators=[DataRequired()])
    CPResp          = StringField('Code Postal du Responsable', validators=[DataRequired()])
    villeResp       = StringField('Ville du Responsable', validators=[DataRequired()])
    telPers         = StringField('Téléphone personnel', validators=[DataRequired()])
    telTrav         = StringField('Téléphone travail')
    mailPers        = StringField('Adresse Mail Personnelle', validators=[DataRequired()])
    mailTrav        = StringField('Adresse Mail de Travail')

class User_ContactForm(FlaskForm):
    nomAuteur       = StringField('Nom Auteur mail', validators=[DataRequired()])
    prenomAuteur    = StringField('Prénom Auteur mail', validators=[DataRequired()])
    mailAuteur      = StringField('Mail Auteur', validators=[DataRequired()])
    objetMessage    = SelectField('Objet', validators=[DataRequired()])
    contenuMessage  = TextField('Contenu message', validators=[DataRequired()])
    pjMessage       = FieldList(FormField(FileField('Pièce-jointe')))

class Admin_ContactForm(FlaskForm):
    objetMessage    = SelectField('Objet', validators=[DataRequired()])
    contenuMessage  = TextField('Contenu message', validators=[DataRequired()])
    pjMessage       = FieldList(FormField(FileField('Pièce-jointe')))

class AutorMedForm(FlaskForm):
    numContactUrg1  = StringField('Numero à contacter Urgence 1', validators=[DataRequired()])
    numContactUrg2  = StringField('Numero à contacter Urgence 2', validators=[DataRequired()])
    numContactUrg3  = StringField('Numero à contacter Urgence 3')

class AutorStage_MineurForm(FlaskForm):
    autorAudioPrive = BooleanField("à effectuer un enregistrement audio de celui-ci dans le cadre du stage de l ensemble de clarinettes 2017.")
    autorAudioPub   = BooleanField('de cet enregistrement audio sur le site Quatuor de clarinettes DIVERTIMENTO (adresse du site) en partie publique')
    autorImag       = BooleanField('à effectuer des photographies et un enregistrement vidéo de celui-ci dans le cadre du stage de ‘ensemble de clarinettes 2017.')
    autorImagSite   = BooleanField('de ces photographies et vidéos sur le site Quatuor de clarinettes DIVERTIMENTO (adresse du site) en partie membres (accès privé par mot de passe)')

class CreateAccountForm(FlaskForm):
    username        = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    mail            = StringField('Adresse mail', validators=[DataRequired()])
    confirmMail     = StringField('Confirmation Adresse Mail', validators=[DataRequired()])
    mdp             = HiddenField('Mot de passe', validators=[DataRequired()])
    mdpConfirm      = HiddenField('Confirmation Mot de passe', validators=[DataRequired()])

class ConnectForm(FlaskForm):
    next            = HiddenField()
    username        = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password        = PasswordField('Mot de passe', validators=[DataRequired()])

    def get_authentificated_user(self):
        user = get_user(self.username.data)
        if user is None:
            return None
        passwd = crypt(self.password.data)
        return user if passwd == user.password else None

class OubliMdpForm(FlaskForm):
    username        = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    mail            = StringField('Adresse mail', validators=[DataRequired()])
    confirmMail     = StringField('Confirmation Adresse Mail', validators=[DataRequired()])

class ModifMdPForm(FlaskForm):
    mdpActu         = HiddenField('Mot de passe actuel', validators=[DataRequired()])
    mdpNew          = HiddenField('Nouvau Mot de passe ', validators=[DataRequired()])
    mdpNewConfirm   = HiddenField('Confirmation nouveau Mot de passe actuel', validators=[DataRequired()])

class StageForm(FlaskForm):
    idSt        = HiddenField('idSt')
    idRep       = HiddenField('idRep')
    intituleSt  = StringField('Intitule du stage', validators=[DataRequired()])
    adresseSt   = StringField('Adresse du stage', validators=[DataRequired()])
    cpSt        = StringField('Code Postal du stage', validators=[DataRequired()])
    villeSt     = StringField('Ville du stage', validators=[DataRequired()])
    nbPlaceSt   = IntegerField('Nombre de places dispos', validators=[DataRequired()])
    dateDebSt   = DateField('Date de début du stage', validators=[DataRequired()])
    dateFinSt   = DateField('Date de fin du stage', validators=[DataRequired()])
    tenueSt     = StringField('Tenue exigée pour le concert du stage')
    prixSt      = FloatField('Prix du stage')
    descStage   = TextField('Description du stage', validators=[DataRequired()])
    nivRequisSt = IntegerField('Niveau minimum pour intégrer le stage')

    # idLieu      = StringField('Adresse', validators[DataRequired()])
