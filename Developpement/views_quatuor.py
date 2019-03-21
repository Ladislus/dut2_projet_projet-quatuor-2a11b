from .views import *

@app.route("/")
def home():
    """

    :return: Retourne le template correspondant a la page de la presentation du quatuor
    """
    return render_template("quatuor/quatuor_presentation.html")

@app.route("/quatuor/presentation/")
def quatuor_presentation():
    """

    :return: Retourne le template correspondant a la page de la presentation du quatuor
    """
    return render_template("quatuor/quatuor_presentation.html")

@app.route("/quatuor/repertoire/")
def quatuor_repertoire():
    """

    :return: Retourne le template correspondant a la page du repertoire du quatuor
    """
    return render_template("quatuor/quatuor_repertoire.html")

gliste=[]
liste2=[]
sliste1=[]
sliste1.append(["Sonate en Sol mineur,"," de Tomaso Albinoni","test.mp3","test.jpg"])
sliste1.append(["Danses hongroises 1,4,5,"," de Johannes Brahms","test.mp3","test.jpg"])
sliste2=[]
sliste2.append(["Suite de danses anglaises - almain*1'15,"," de William Byrd","almain.mp3","test.jpg"])
sliste2.append(["Suite de danses anglaises - pavan*1'20,"," de William Byrd","pavan.mp3","test.jpg"])
sliste2.append(["Suite de danses anglaises - galliard*0'56,"," de William Byrd","galliard.mp3","test.jpg"])
liste2.append(sliste1)
liste2.append(sliste2)
gliste.append(liste2)
liste3=[]
sliste3=[]
sliste3.append(["Quatuor n°2 en mi bémol majeur - poco adagio-allegro*6'18,"," de B.H. Crusell","pocoadagio.mp3","test.jpg"])
sliste3.append(["Quatuor n°2 en mi bémol majeur - romance*4'07,"," de B.H. Crusell","romance.mp3","test.jpg"])
sliste3.append(["Quatuor n°2 en mi bémol majeur - menuet, allegro*2'50,"," de B.H. Crusell","menuet.mp3","test.jpg"])
sliste3.append(["Quatuor n°2 en mi bémol majeur - allegro vivace*3'17,"," de B.H. Crusell","allegro.mp3","test.jpg"])
sliste4=[]
sliste4.append(["Golliwogg's cake walk,"," de Claude Debussy","golliwogg's-01.mp3","test.jpg"])
sliste4.append(["Le petit nègre,"," de Claude Debussy","test.mp3","test.jpg"])
liste3.append(sliste3)
liste3.append(sliste4)
gliste.append(liste3)
@app.route("/quatuor/extrait/<int:id>")
def quatuor_extrait(id):
    """

    :return: Retourne le template correspondant a la page des extraits du quatuor
    """
    ok=False
    if len(gliste)>1:
        ok=True


    return render_template("quatuor/quatuor_extrait.html",liste=gliste,ok=ok,id=id)

@app.route("/quatuor/extrait/ajout/")
def quatuor_extrait_ajout():
    """

    :return: Retourne le template correspondant a la page de creation des extraits du quatuor
    """
    return render_template("",);



liste=[]
liste.append(["Le Quatuor a un nouveau site Web","22/12/2018","Olivier Roussillat","presentation-quatuor-1","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine e dico."])
liste.append(["Le Groupe 2A11b a fait le meilleur site web","23/12/2018","Sophie Anglade","presentation-quatuor-2","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine e dico."])
liste.append(["Car c'est notre projet!","24/12/2018","Andrien Foucault","presentation-quatuor-3","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine e dico."])
liste.append(["Un nouveau départ","12/01/2018","Michael Abid","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine e dico."])
liste.append(["Deux nouveaux départs","13/01/2018","Michael Abid","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine e dico."])
liste.append(["Trois nouveaux départs","14/01/2018","Alexis Chauvette","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine e dico."])
liste.append(["Quatre nouveaux départs","12/01/2018","Michael Abid","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine e dico."])
liste.append(["Cinq nouveaux départs","13/01/2018","Michael Abid","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine e dico."])
liste.append(["Six nouveaux départs","14/01/2018","Alexis Chauvette","fond","Omitto iuris dictionem in libera civitate contra leges senatusque consulta; caedes relinquo; libidines praetereo, quarum acerbissimum extat indicium et ad insignem memoriam turpitudinis et paene ad iustum odium imperii nostri, quod constat nobilissimas virgines se in puteos abiecisse et morte voluntaria necessariam turpitudinem depulisse. Nec haec idcirco omitto, quod non gravissima sint, sed quia nunc sine e dico."])

@app.route("/quatuor/presse/actu/")
def quatuor_presse_actu():
    """

    :return: Retourne le template correspondant a la page des articles de presse du quatuor actuelle
    """
    return render_template("quatuor/quatuor_presse_actu.html",liste=liste)



@app.route("/quatuor/presse/all/<int:id>")
def quatuor_presse_all(id):
    """

    :return: Retourne le template correspondant a la page de touts les articles de presse en rapport avec le quatuor
    """
    ok=False
    listetrois=[]
    listetrois.append(liste[0])
    listetrois.append(liste[1])
    listetrois.append(liste[2])
    glistR=[]
    listeR=[]
    cpt=-1
    for elem in liste:
        cpt+=1
        listeR.append(elem)
        if cpt==5:
            cpt=0
            glistR.append(listeR)
            listeR=[]
    if listeR:
        glistR.append(listeR)
    page=[]
    try:
        page=glistR[id]

    except Exception as e:
        page=glistR[0]

    if len(glistR)>1:
        ok=True


    return render_template("quatuor/quatuor_presse_all.html",liste=page,caroussel=listetrois,id=id,ok=ok)


@app.route("/quatuor/presse/article/<nomarticle>")
def quatuor_presse(nomarticle):


    """
    :id: L'id de l'article de presse
    :return: Retourne le template correspondant a la page d'un artciel du quautor
    """
    article=None
    for elem in liste:
        if elem[0]==nomarticle:
            article=elem
    if article==None:
            return render_template("other/page_404.html")
    return render_template("quatuor/quatuor_presse.html",article=article)
