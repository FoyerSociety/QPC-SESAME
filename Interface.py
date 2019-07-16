#-*-coding: Utf-8 -*-
# __author__: Gaetan Jonathan BAKARY

from tkinter import * 
import tkinter.font as tkFont
import tkinter.messagebox as tkmsg
import time, json, random
import moduleQPC  #  nos propres modules

i = j = 0  #  compteur utile
dictionnaire = {}


class InterJeu:
    def __init__(self):
        """
            class mere d'une ouverture de fenetre de jeu 
                dans le but de ne pas reécrire chque init pour chaque code
                                                                            """
        self.root = Tk()  #  creation de ma fenetre
        self.root.config(bg='white')  #  fond blanc 
        self.root.geometry('1200x600+0+0')  # taille de la fenetre 
        self.root.wm_state(newstate="zoomed")  #  plein ecran windows
        #self.root.resizable(width=False, height=False)


        
class Interface():
    def __init__(self):
        """
            Constructeur de la classe Interface   
                                                    """
        self.root = Tk()  #  creation de ma fenetre
        self.root.title('Menu Principale')
        self.root.geometry('1200x600+100+50')  # taille de la fenetre + position
        self.root['bg'] = 'white'  # couleur du fond 
        self.root.resizable(width=False, height=False)  #  empecher le redimensionnement
        #  ci dessous sont variable contenant des fonts
        self.helv32 = tkFont.Font(family='Helvetica', size=32, weight='bold')
        self.helv36 = tkFont.Font(family='Arial', size=36, weight='bold')
        self.arial24 = tkFont.Font(family='Arial', size=22, weight='bold')
        self.arial12 = tkFont.Font(family='Arial', size=12, weight='bold')
        self.verdana30 = tkFont.Font(family='Verdana', size = 30, weight = 'bold')
        self.arialinfo0 = tkFont.Font(family='Arial', size=18)
        self.arialinfo = tkFont.Font(family='Arial', size=16)
        self.arialinfo14 = tkFont.Font(family='Arial', size=14)
        #  ci dessous est variable contenant les images en taille initiale
        self.offline0 = PhotoImage(file='Images\offline.png')
        self.poussoir0 = PhotoImage(file='Images\poussoir.png')
        self.fsociety0 = PhotoImage(file='Images\logo.png')
        self.esti0 = PhotoImage(file='Images\esti.png')
        self.backImage0 = PhotoImage(file='')
        self.sesame0 = PhotoImage(file='Images\sesame.png')
        self.reseau0 = PhotoImage(file='Images\\reseau.png')
        self.projet0 = PhotoImage(file='Images\projet.png')
        self.setting0 = PhotoImage(file='Images\settings.png')
        #  initialisation d'un compteur
        self.count = 0  
         

    def __corps__(self):
        """
            Methode contenant le corps de l'Interface principal
                                                                    """
        #  creation et positionnement d'un canvas et son contenu
        self.eval = Canvas(self.root, bg = 'white', width = 1200, height = 75)
        self.eval.place(relx = -0.001, rely = -0.001)
        self.eval.create_text(602, 38 , text = 'Question Pour un Champion', font = self.verdana30, fill = 'teal')  #  creation du titre en tant que text
        #  redimensonnement des images
        self.fsociety = self.fsociety0.subsample(8, 8)
        self.sesame = self.sesame0.subsample(20, 20)  #  image redimensionner 
        #  ajout de contenu supll 
        self.eval.create_image(90, 40 , image = self.fsociety) 
        self.eval.create_image(1140, 37 , image = self.sesame)  #  nametraka image a un position 
        #  creation de canvas de bas et sa position 
        self.footer = Canvas(self.root, bg = 'teal', width = 1202, height = 50, bd = 0, highlightthickness = 0)  #  canvas en bas 
        self.footer.place(relx = -0.001, rely = 0.92)  #  sa position 
        # ci dessous les elements a placé sur le canvas
        self.footer.create_text(1120, 25, text = '© Copyright Juin 2019', activefill = 'orange', fill ='yellow')
        self.footer.create_text(105, 25, text = '♣ Licence Libre & Open Source ♣', activefill = 'orange', fill ='yellow')
        self.footer.create_text(600, 25, text = '☻ ambatoroka.fsociety@gmail.com ☻', activefill = 'orange', fill ='yellow')
        #  creation de canvas de jeu 
        self.menuJeu = Canvas(self.root, bg = 'teal', highlightthickness = 0, width = 1202, height = 65)
        self.menuJeu.place(relx = - 0.001, rely = 0.1278)  #  canvas pour les choix de mode de jeu 
        #  Ci dessous la creation du bouton mode offline avec ses comportements
        self.offlineButton = Button(self.root, bd = 0, fg = 'yellow', cursor ='hand2', relief = 'groove',  bg = 'teal', activeforeground = 'yellow', activebackground = 'teal', text = "Mode Offline",  font = self.arial24, command = self.offlineCommand)
        self.offlineButton.place(relx = 0.005, rely = 0.13)
        self.offlineButton.bind("<Enter>", self.offlinemouseOverEnter)  # evenement survole le souris lance la fonction precisé
        self.offlineButton.bind("<Leave>", self.offlinemouseOverLeave)  #  evenement contraire du celle du dessus
    

    def fen_f1Close(self):
        """ 
            fonction servant a intercepter la fermeture
                de la fenetre de fen f1 pour renitiliser le compteur 
                                                                    """
        self.count = 0  #  retour au zero du compteur
        self.fen_f1.destroy()  #  detruire la fenetre


    def openProject(self):
        """
            fonction permettant d'ouvrir un projet
                de question et de verifier si le fichier est valide
                                                                    """ 
        self.fen_f1.destroy()  #  destruction de la fenetre
        self.count = 0  #  renitialisation du compteur
        self.file = moduleQPC.recupfichier(extension = 'qpc')  #  ouverture de l explorer
        #  verification si un fichier a été selectionner
        if self.file is not '':  #  si un fichier a ete selectionner
            f = open(self.file, 'r', encoding = 'utf8')  #  ouvrir en mode lecture seule
            try:
                self.dict = json.load(f)  #  transform en dictionnaire les données 
            except:  #  si erreur , fichier corrompu ou pas valide 
                tkmsg.showwarning('Fichier non valide', 'Attention, veuillez selectionner le bon fichier...\n Le fichier est peut être endommagé')
                self.root.withdraw()  #  cache la fenetre principale
                self.root.deiconify()  #  reafficher la fenetre 
            else:  #  si tous c est bien passé 
                self.root.quit()  #  quitter  l interface
                self.root.destroy()  #  assurer sa destruction 
                global dictionnaire  #  atteindre la variable global
                dictionnaire = self.dict   #  assigner les données
                offlineStart()  #  lancer l interface de jeu
        else:   #  cas d une annulation
            #  rendre en premier plan la fenetre
            self.root.withdraw()
            self.root.deiconify()

    
    def newProject(self):
        """
            fonction permettant de lancer un nouveau projet de question 
                dans le but de creer une nouvelle fenetre pour entrer les questions et les reponses
                                                                                                    """
        self.count = 0  #  renitialiser le compteur 
        self.dict = {}  #  initialiser un variable qui va contenir tous les données
        self.dict['Question1'] = []  #  initialiser une liste dans le dict pour les questions niveau1
        self.dict['Reponse1'] = []  #  pour les reponses niveau1
        #  une petite formatage de texte
        self.dict['Question2'] = []  #  pour les questions niveau1
        self.dict['Reponse2'] = []  #  pour les reponses niveau1
        #  une petite formatage de texte
        self.dict['Question3'] = []  #  pour les questions niveau3
        self.dict['Reponse3'] = []  #  pour les reponses niveau3
        #  ci dessous la creation de la fenetre fille 
        self.fen_f1.destroy()  # destruction de la fenetre de choix 
        self.fen_ques1 = Toplevel(self.root)   #  creation d une fenetre fille de fenetre principal
        self.fen_ques1.title('QPC SESAME: Question')  #  titre du fenetre
        self.fen_ques1['bg'] = 'white'  #  couleur de fond 
        self.fen_ques1.geometry('700x500+400+100')   #  taille et position de la fenetre
        self.fen_ques1.protocol("WM_DELETE_WINDOW", self.fen_quesClose)   #   un protocol qui intercepte la fermeture de la fenetre 
        #  ci dessous creation des widgets presents dans la fenetre
        self.fen_ques1Topnav = Canvas(self.fen_ques1, width = 705, height = 35, bg = 'white')
        self.fen_ques1Aftnav = Canvas(self.fen_ques1, width = 705, height = 35, bg = 'teal', highlightthickness = 0)
        self.fen_ques1Topnav.place(relx = -0.00001, rely = 0.01)
        self.fen_ques1Aftnav.place(relx = -0.00001, rely = 0.08)
        self.fen_ques1Topnav.create_text(330, 18, text = 'Projet Questions', font = self.arialinfo14, fill = 'teal')
        #  ci dessous mise en place du radio button pour le choix de niveau 
        self.etiquette = ['Niveau 1', 'Niveau 2', 'Niveau 3']  #  le texte sur le radio 
        self.values = [1 , 2 , 3]  # ses valeurs initial selon l ordre du nom 
        self.niveau = IntVar()  #  variable qui va recuperer le choix 
        for i in range(3):  #  positionnement du radio 
            self.Rniveau = Radiobutton(self.fen_ques1, variable = self.niveau, text = self.etiquette[i], value = self.values[i], font = self.arialinfo14)
            self.Rniveau.place(relx =(0.1+(i*0.3)), rely = 0.2)
        del i  
        self.champQuestion = Text(self.fen_ques1, height = 6, width = 70, bg = 'lightgray')   #  mise en place du champ de question 
        self.champQuestion.place(relx = 0.1, rely = 0.35)
        self.champQuestion.insert('1.0', "Enter la question...")   #  le texte sur le champ 
        self.champQuestion.bind("<Button-1>", self.champQuestionOverEnter)  #  evenement lancer au click du champ pour effacer le texte
        #  mise en place du champ de reponse 
        self.reponse = StringVar()  #  variable recuperant le texte entré 
        self.reponse.set('Entrer la réponse... ')  #  le texte a afficher 
        self.champReponse = Entry(self.fen_ques1,  textvariable = self.reponse, width = 50, bg = 'lightgray', font = self.arialinfo14, fg = '#333')
        self.champReponse.place(relx = 0.1, rely = 0.6)
        self.champReponse.bind("<Button-1>", self.champReponseOverEnter)  #  evenement au click du champ reponse pour effacer le texte
        #  creation et positionnement des boutons et la fonction relier a son action
        self.enrButton = Button(self.fen_ques1, text = 'Enregistrer', font = self.arialinfo, command = self.enregistrer)
        self.enrButton.place(relx = 0.1, rely = 0.7)
        self.verButton = Button(self.fen_ques1, text = 'Verifier', font = self.arialinfo, command = self.verifier)
        self.verButton.place(relx = 0.77, rely = 0.7)
        self.termButton = Button(self.fen_ques1, text = 'TERMINER',font = self.arialinfo14, fg = 'teal', command = self.terminer)
        self.termButton.place(relx = 0.42, rely = 0.85)
        #  ci dessus creation des bouttons images qui permets de configurer le nombre de point de chaque niveau 
        self.setting = self.setting0.subsample(2, 2)  #  redimensionnement de l image 
        #  placement des boutons pour le niveau 1
        self.niveau1Set = Button(self.fen_ques1, image = self.setting, highlightthickness = 0 , bg = 'white', bd = 0, command = self.changeValue1)
        self.niveau1Set.place(relx = 0.25,rely = 0.21)
        #  placement des boutons pour le niveau 2
        self.niveau2Set = Button(self.fen_ques1, image = self.setting, highlightthickness = 0 , bg = 'white', bd = 0, command = self.changeValue2)
        self.niveau2Set.place(relx = 0.55,rely = 0.21)
        #  placement des boutons pour le niveau 3
        self.niveau3Set = Button(self.fen_ques1, image = self.setting, highlightthickness = 0 , bg = 'white', bd = 0, command = self.changevalue3)
        self.niveau3Set.place(relx = 0.85,rely = 0.21)
        

    def changeValue1(self):
        """
            fonction reagissant a un boutton pour 
                changer les point des questions de niveau 1 
                                                            """
        self.fenVal1 = Toplevel(self.fen_ques1)  #  ouverture d'une petite fenetre
        self.fenVal1.title("Point d'incrémentation")   #  titr de la fenetre
        self.fenVal1.geometry('+500+250')  # sa position 
        self.valeur1 = IntVar()  #  variable recuperant le nouveau valeur 
        #  ci dessous la configuration des widgets
        label = Label(self.fenVal1, text = 'Entrer le nombre de point du question "Niveau 1" ').pack()
        entre = Entry(self.fenVal1, textvariable = self.valeur1)
        self.valeur1.set(self.values[0])
        entre.pack()
        #  creation du bouton pour prendre la nouvelle valeur
        boutton = Button(self.fenVal1, text = 'Valider', width = 20, command = self.getValue1).pack()


    def changeValue2(self):
        """
            fonction reagissant a un boutton pour 
                changer les point des questions de niveau 2 
                                                            """
        self.fenVal2 = Toplevel(self.fen_ques1)   #  ouverture d'une petite fenetre
        self.fenVal2.title("Point d'incrémentation")
        self.fenVal2.geometry('+550+250')
        self.valeur2 = IntVar()  #  variable recuperant le nouveau valeur
        #  ci dessous la configuration des widgets
        label = Label(self.fenVal2, text = 'Entrer le nombre de point du question "Niveau 2" ').pack()
        entre = Entry(self.fenVal2, textvariable = self.valeur2)
        self.valeur2.set(self.values[1])
        entre.pack()
        #  creation de bouton pour prendre la nouveau valeur
        boutton = Button(self.fenVal2, text = 'Valider', width = 20, command = self.getValue2).pack()
    
    
    def changevalue3(self):
        """
            fonction reagissant a un boutton pour 
                changer les point des questions de niveau 3 
                                                            """
        self.fenVal3 = Toplevel(self.fen_ques1)   #  ouverture d'une petite fenetre
        self.fenVal3.title("Point d'incrémentation")
        self.fenVal3.geometry('+550+250')
        self.valeur3 = IntVar()   #  variable recuperant le nouveau valeur
        #  ci dessous la configuration des widgets
        label = Label(self.fenVal3, text = 'Entrer le nombre de point du question "Niveau 3" ').pack()
        entre = Entry(self.fenVal3, textvariable = self.valeur3)
        self.valeur3.set(self.values[2])
        entre.pack()
         #  creation de bouton pour prendre la nouveau valeur
        boutton = Button(self.fenVal3, text = 'Valider', width = 20, command = self.getValue3).pack()


    def getValue1(self):
        """
            fonction pour changer les valeurs du  RadioBoutton1
                                                                """
        self.values[0] = self.valeur1.get()  #  recuperation de nouvelle valeur
        self.Rniveau.destroy()  #  destruction des widgets
        self.fenVal1.destroy()
        self.valeur1.set(self.values[0])
        for i in range(3):  # reconstruction des widgets
            self.Rniveau = Radiobutton(self.fen_ques1, variable = self.niveau, text = self.etiquette[i], value = self.values[i], font = self.arialinfo14)
            self.Rniveau.place(relx =(0.1+(i*0.3)), rely = 0.2)

    
    def getValue2(self):
        """
            fonction pour changer les valeurs du  RadioBoutton2
                                                                """
        self.values[1] = self.valeur2.get()  #  recuperation de la nouvelle valeur 
        self.Rniveau.destroy()  #  destruction pour la reconstrucution
        self.fenVal2.destroy()
        self.valeur2.set(self.values[1])  #  afficher sa nouvelle valeur 
        for i in range(3):  #  reconstruction 
            self.Rniveau = Radiobutton(self.fen_ques1, variable = self.niveau, text = self.etiquette[i], value = self.values[i], font = self.arialinfo14)
            self.Rniveau.place(relx =(0.1+(i*0.3)), rely = 0.2)


    def getValue3(self):
        """
            fonction pour changer les valeurs du  RadioBoutton3
                                                                """
        self.values[2] = self.valeur3.get()  #  recuperation de la nouvelle valeur 
        self.Rniveau.destroy()  #  destruction pour une reconstruction 
        self.fenVal3.destroy()
        self.valeur3.set(self.values[2])
        for i in range(3):  #  reconstruction avec ses nouvelles valeurs
            self.Rniveau = Radiobutton(self.fen_ques1, variable = self.niveau, text = self.etiquette[i], value = self.values[i], font = self.arialinfo14)
            self.Rniveau.place(relx =(0.1+(i*0.3)), rely = 0.2)

    
    def enregistrer(self):
        """
            une fonction permettant d enregistrer temporairement 
                dans la RAM , les questions et reponses entrées dans le projet
                                                                                """
        
        remise = True
        effacer = True  #  initialisation d une variable de verification 
        textget = self.champQuestion.get('1.0','10.0')  #  recupere l entré du champ question 

        if self.niveau.get() == self.values[0]:  #  si la question est de niveau 1
            #  ajout des données
            self.dict['Question1'].append([textget, len(textget.strip())])  
            self.dict['Reponse1'].append([self.reponse.get().strip(), self.niveau.get()])

        elif self.niveau.get() == self.values[1]: #  si la question est de niveau 2
            #  ajout des donnée
            self.dict['Question2'].append([textget, len(textget.strip())])
            self.dict['Reponse2'].append([self.reponse.get().strip(), self.niveau.get()])

        elif self.niveau.get() == self.values[2]:  #  si la question est de niveau 3
            #  ajout des donnée
            self.dict['Question3'].append([textget, len(textget.strip())])
            self.dict['Reponse3'].append([self.reponse.get().strip(), self.niveau.get()])

        else:  #  si aucun niveau n a été selectionner 
            tkmsg.showwarning('Aucun niveau selectionné', "Attention,\nIl est impératif de selectionner le niveau de cette question")
            #  reaaffiche la fenetre 
            self.fen_ques1.withdraw()
            self.fen_ques1.deiconify()
            effacer = False   #  ne pas vider le champ car pas encore enregistrer
            remise = False

        if effacer:  #  si tous c est bien passé 
            #  effacer les données
            self.reponse.set('')  #  vider le champ
            self.champQuestion.delete('1.0', '10.0')  #  vider le champ

        if remise:
            global i
            global j 
            i = j = 0 
            self.champQuestion.insert('1.0', "Enter la question...")
            self.reponse.set('Entrer la réponse... ')
        
        del effacer

        

    
    def verifier(self):
        """ 
            fonction permettant de verifier tous les questions
                 avant de terminer pour but d'eviter toute heure durant le jeu
                                                                                """
        self.fen_ver = Toplevel(self.fen_ques1)  #  creation d une fenetre fille 
        self.fen_ver.title('Verification')  #  titre de cette nouvelle fenetre
        self.fen_ver.config(bg = 'lightgray')
        self.qrp = StringVar()  #  variable contenant le retour et l entré du liste
        #  methode pour entrer les questions et reponses dans des listes
        q1 = []  #  initialisation d'une liste contenant les questions de types niveau 1 
        for x in self.dict['Question1']:
            q1.append(x[0].replace('\n', ''))  #  ajout des questions de niveau1 dans la liste 
        r1 = []  #  initialisation d'une liste contenant les reponses de types niveau 1  
        for x in self.dict['Reponse1']:
            r1.append((x[0], x[1]))  #  ajout des reponses de niveau 1 dans la liste
        #  même technique que dessus 
        q2 = []
        for x in self.dict['Question2']:
            q2.append(x[0].replace('\n', ''))
        r2= []
        for x in self.dict['Reponse2']:
            r2.append((x[0], x[1]))
        
        q3 = []
        for x in self.dict['Question3']:
            q3.append(x[0].replace('\n', ''))
        r3 = []
        for x in self.dict['Reponse3']:
            r3.append((x[0], x[1]))
        #  ajout des questions et reponses dans une seule variable  et formatage du texte
        tmp = []  #  variable temporaire contenant l ensembles des choses a afficher
        #  pour le niveau  1
        i = 1
        for x in range(1, len(self.dict['Question1']) + 1):
            tmp.append(f"1-{i}) {q1[x-1]}")
            tmp.append(f"--> {r1[x-1][0]} :    {r1[x-1][1]} points")
            tmp.append([])
            i += 1
        #  pour le niveau 2
        i = 1
        for x in range(1, len(self.dict['Question2']) + 1):
            tmp.append(f"2-{i}) {q2[x-1]}")
            tmp.append(f"--> {r2[x-1][0]} :    {r2[x-1][1]} points")
            tmp.append([])
            i += 1
        #  pour le niveau 3
        i =  1
        for x in range(1, len(self.dict['Question3']) + 1):
            tmp.append(f"3-{i}) {q3[x-1]}")
            tmp.append(f"--> {r3[x-1][0]} :    {r3[x-1][1]} points")
            tmp.append([])
            i += 1

        self.qrp.set(tmp)  #  insertion dans la liste  
        #  Mise en place des scrollbar pour les longs textes
        yDefilB = Scrollbar(self.fen_ver, orient='vertical')
        yDefilB.grid(row=0, column=1, sticky='ns')
        xDefilB = Scrollbar(self.fen_ver, orient='horizontal')
        xDefilB.grid(row=1, column=0, sticky='ew')
        #  creation de la liste 
        self.listes = Listbox(self.fen_ver, xscrollcommand = xDefilB.set,  yscrollcommand = yDefilB.set, listvariable = self.qrp, width = 100, height = 20, activestyle = 'dotbox', selectforeground = 'yellow')
        self.listes.grid(row=0, column=0, sticky='nsew')  # positionnement dans la fenetre
        #  les actions des scrollbar 
        xDefilB['command'] = self.listes.xview  
        yDefilB['command'] = self.listes.yview
        #  evenement a un clique droite de la souris
        self.listes.bind('<Button-3>', self.verifConfig)
        #  evenement a un clique gauche de la souris
        self.listes.bind('<Button-1>', self.clickclose)


    def clickclose(self, event):
        #  fonction permettant de fermer l'option clique droite du souris 
        try:
            self.option.destroy()   #  detruire s'il existe
        except:  #  si erreur ( si il n existe pas)
            pass  #  rien faire 


    def terminer(self):
        #  ouverture de l'explorateur pour la sauvegarde
        self.file = moduleQPC.saveFichier(defaultextension = '.qpc', initialfile = 'project1.qpc', title = 'Sauvegarde du projet')
        #  gestion des erreurs par des conditions
        if self.file is not '':  #  cas d une non  annulation 
            with open(self.file, 'w', encoding = 'utf8') as json_data:  #  ouvrir le fichier creer en mode ecriture 
                json.dump(self.dict, json_data, indent = 4, ensure_ascii = False)  #  parse dans le fichier creer le  dictionnaire des questions 
            self.fen_ques1.destroy()  #  detruire la fenetre 
            self.root.quit()
            self.root.destroy()
            global dictionnaire 
            dictionnaire = self.dict 
            #  lancer le jeu offline
            offlineStart()
        else:  #  cas d une annulation 
            #  reaffiche la fenetre 
            self.fen_ques1.withdraw()
            self.fen_ques1.deiconify()


    def verifConfig(self, event):
        """
            fonction lancer a partir d un evenement
                de clique droite de la souris qui a pour but 
                    de modifier ou de suprimé une question ou une une reponse
                                                                                """
        try:
            self.option.destroy()  #  detruire si il existe déja pour eviter les clones 
        except:
            pass  #  si erreur , ne fait rien 
        else:  #  si tous c'est bien passé, ne fait rien 
            pass
        #  nouveau bloc d essaie 
        try:  
            int(self.listes.curselection()[0])   #  transformer en integer si possibe 
        except:
            #  dans ce cas d erreur , rien n est selectionner
            pass 

        else:  #  si aucun erreur a été declenché 
            if (int(self.listes.curselection()[0])) % 3 == 2:  #  si la case vide a été selectionner 
                pass
            else:  #  si la case question ou reponse 
                #  creation d'un cadre pour mettre les option 
                self.option = Frame(self.fen_ver, cursor = 'hand2', bd = 5, highlightcolor = 'orange', highlightthickness = 2, bg ='teal')
                pointX1 = self.fen_ver.winfo_pointerx()  #  position de la pointe de souris par rapport a l horizontale de l'ecran
                pointX0 = self.fen_ver.winfo_x()  #  position top du fenetre par rapport a l horizontal de l ecran
                pointY1 = self.fen_ver.winfo_pointery()  #  position de la pointe de souris par rapport a la verticale de l'ecran
                pointY0 = self.fen_ver.winfo_y() + 10  #  position top du fenetre par rapport a la verticale  de l ecran ajuster par 10px 
                #  creation des cavas qui va se comporter comme un bouton 
                self.mod = Canvas(self.option, bg = 'teal', width = 60, height = 25, bd = 0 , highlightthickness = 0)
                self.mod.create_text(30, 10 , text = 'Modifier', fill = 'yellow', activefill = 'orange')
                self.mod.pack()
                #  creation des cavas qui va se comporter comme un bouton
                self.eff = Canvas(self.option, bg = 'teal', width = 60 , height = 25, bd = 0 , highlightthickness = 0)
                self.eff.create_text(30, 12 , text = 'Supprimer', fill = 'yellow', activefill = 'orange')
                self.eff.pack()
                #  decorer par une ligne entre les deux canvas 
                self.mod.create_line(0, 24, 60, 24, fill = 'white', width = 2)
                self.option.place(x = pointX1 - pointX0, y = pointY1 - pointY0)
                #  evenement a un click des deux canvas 
                self.mod.bind('<Button-1>', self.modverifier)
                self.eff.bind('<Button-1>', self.effverifier)


    def modverifier(self, event):
        """
            fonction declenché a partir d un click sur le canvas modifier 
                permettent de modifier le texte cliqué soit la question ou la reponse
                                                                                        """
        self.option.destroy()  #  detruire l'option du clique droite
        self.moded = self.listes.get(self.listes.curselection())  #  prendre l'index de la partie selectionner 
        #  ci dessous pour verifier si partie question ou partie reponse
        if (int(self.listes.curselection()[0])) % 3 == 0:  #  partie question
            question_detect = self.moded.split(')')[1].strip()  #  recuperer que le texte de la  question 
            detect = self.moded.split(' ')[0]  #  recuperer son identification
            detect = detect[:len(detect) - 1]
            self.popedit(question_detect, detect, 'question')  #  appel la fonction qui edit le contenur le voulue
        
        elif (int(self.listes.curselection()[0])) % 3 == 1:  #  partie reponse 
            reponse_detect = self.moded.split('>')[1].split(':')[0].strip()  # recupere que le texte de la reponse
            #  prendre l'index de la question relié pour identifer l emplacement dans le dictionnaire
            self.moded = self.listes.get(int(self.listes.curselection()[0]) - 1)  
            detect = self.moded.split(' ')[0]  #  recuperer son identification
            detect = detect[:len(detect) - 1]
            self.popedit(reponse_detect, detect, 'reponse')  #  appel la fonction qui edit le contenur le voulue


    def popedit(self, chose, emp, choix):
        """
            fonction permettant d'afficher une fenetre
                qui sert a entrer la modification de la chose selectionner
                                                                           """
        self.detect = emp   
        self.fenmod = Toplevel(self.fen_ver)  #  creation d'une nouvelle fenetre
        self.fenmod.config(bg ='white')
        #  creation des widgets pour remplir le nouveau contenue 
        decor = Canvas(self.fenmod, width = 400, height = 40, bg = 'teal', bd = 0, highlightthickness = 0)
        decor.create_text(200, 20, text = 'MODIFICATION', fill = 'yellow', font = self.arialinfo)
        decor.pack()
        labelold = Label(self.fenmod, text = '\nAncien contenu:\n', bg = 'white', font = self.arial12).pack()
        choseOld = Text(self.fenmod, fg = 'red', height = 4, width = 50, bg = 'lightgray')
        choseOld.pack()
        labelresp = Label(self.fenmod, text = '\nEntrer Nouveau contenu:\n', bg ='white', font = self.arial12).pack()
        self.entreques = Text(self.fenmod,  width = 50, height = 4, bg = 'lightgray', fg ='darkgreen')
        self.entreques.pack()
        #  boutton permettant de recuperer la nouvelle contenue
        butterm = Button(self.fenmod, text = 'Terminer Changement', font = self.arialinfo14, command = lambda: self.enregChange(choix)).pack(pady = 15)
        choseOld.insert('1.0', chose)  # inserer l'ancien contenu dans un champ 


    def enregChange(self, choix):
        """
            fonction declenché par le boutton Terminer changement
                dans le but de recuperer le nouveau contenue et de mettre a jour le dict
                                                                                         """
        if choix == 'question':  #  si c est la question qu il faut mettre a jour 
            if int(self.detect[0]) == 1:  #  question de niveau 1 
                #  mettre a jour le dictionnaire de données
                self.dict['Question1'][int(self.detect[2]) - 1][0] = self.entreques.get('1.0', '10.0').strip()  
            elif int(self.detect[0]) == 2:  #  question de niveau 2 
                #  mettre a jour le dictionnaire de données
                self.dict['Question2'][int(self.detect[2]) - 1][0] = self.entreques.get('1.0', '10.0').strip() 
            elif int(self.detect[0]) == 3:  #  question de niveau 3 
                #  mettre a jour le dictionnaire de données
                self.dict['Question3'][int(self.detect[2]) - 1][0] = self.entreques.get('1.0', '10.0').strip()
        #  espacement  
        elif choix == 'reponse':  #  si c est la reponse qu il faut mettre a jour
            if int(self.detect[0]) == 1: #  reponse niveau 1
                # mettre a jour le dictionnaire de données
                self.dict['Reponse1'][int(self.detect[2]) - 1][0] = self.entreques.get('1.0', '10.0').strip()
            elif int(self.detect[0]) == 2:  #  reponse niveau 2
                # mettre a jour le dictionnaire de données
                self.dict['Reponse2'][int(self.detect[2]) - 1][0] = self.entreques.get('1.0', '10.0').strip()
            elif int(self.detect[0]) == 3:  #  reponse niveau 3
                # mettre a jour le dictionnaire de données
                self.dict['Reponse3'][int(self.detect[2]) - 1][0] = self.entreques.get('1.0', '10.0').strip()
        #  detruite la fenetr apres finissions et relancer la fenetre de verification pour la mise a jour
        self.fen_ver.destroy()
        self.verifier()


    def effverifier(self, event):
        """
            focntion permettant d'effacer une question et sa reponse
                ou vise versa dans le but d'éliminer les sources d'erreur 
                                                                            """
        self.option.destroy()  #  detruire d'abord la fenetre

        if (int(self.listes.curselection()[0])) % 3 == 0:  #  si c est une question qui a ete selectionner
            self.moded = self.listes.get(self.listes.curselection())
            detect = self.moded.split(' ')[0]  #  recuperer son identification
            detect = detect[:len(detect) - 1]

            if int(detect[0]) == 1: #  si l index est dans la question 1 
                self.dict['Question1'].pop(int(detect[2]) - 1)  #  efface la question
                self.dict['Reponse1'].pop(int(detect[2]) - 1)  #  efface la reponse associé
            elif int(detect[0]) == 2:  #  si l index est dans la question 2
                self.dict['Question2'].pop(int(detect[2]) - 1)  #  efface la question 
                self.dict['Reponse2'].pop(int(detect[2]) - 1)  #  efface la reponse associé 
            elif int(detect[0]) == 3:  #  si l index est dans la question 3
                self.dict['Question3'].pop(int(detect[2]) - 1)   #  efface la question
                self.dict['Reponse3'].pop(int(detect[2]) - 1)  #  efface le reponse 

        elif (int(self.listes.curselection()[0])) % 3 == 1:  #  si c est une reponse qui a ete selectionner
            self.moded = self.listes.get(int(self.listes.curselection()[0]) - 1)
            detect = self.moded.split(' ')[0]
            detect = detect[:len(detect) - 1]
            
            if int(detect[0]) == 1: #  si l index est dans la question 1
                self.dict['Reponse1'].pop(int(detect[2]) - 1)  #  efface la reponse 
                self.dict['Question1'].pop(int(detect[2]) - 1) #  efface la question associé 
            elif int(detect[0]) == 2: #  si l index est dans la question 2
                self.dict['Reponse2'].pop(int(detect[2]) - 1)  #  efface la reponse
                self.dict['Question2'].pop(int(detect[2]) - 1)  #  efface la question associé
            elif int(detect[0]) == 3: #  si l index est dans la question 3
                self.dict['Reponse3'].pop(int(detect[2]) - 1)  #  efface la reponse 
                self.dict['Question3'].pop(int(detect[2]) - 1)   #  efface la question associé
        #  detruite la fenetr apres finissions et relancer la fenetre de verification pour la mise a jour
        self.fen_ver.destroy()
        self.verifier()


    def fen_quesClose(self):
        """
            fonction appeler en cas de fermeture de la fenetre d entrer de question
                                                                                    """
        allow = 0  #  initialisation de compteur 
        authorize = False  #  initialisation de variable de verification 
        for test in self.dict.values():  #  iterer tous les valeurs du dict contenant les données
            if (test != []):  #  au cas ou elle n'est est vide 
                allow += 1   #  incrementer le compteur 
        if allow > 0:  #  si les données ne sont pas vide 
            rep = tkmsg.askquestion("Confirmer la fermeture", "les données seront perdues si vous continuez...\n Voulez-vous quand même fermer?")
            if rep == 'yes':
                authorize = True  #  autoriser la fermeture 
            else:
                self.fen_ques1.withdraw()  #  reaffiche la fenetre
                self.fen_ques1.deiconify() 
            del rep  #  efface la varible qui ne sera plus utile 
        else:   #  si les données sont vides 
            authorize = True  #  autoriser la fermeture 

        if authorize:  #  si authorise est vrai 
            global i
            global j
            i = j = 0  #  renitialiser le compteur 
            self.fen_ques1.destroy()  #  detruitr la fenetre 
        
        del allow, authorize   #  deletion des variables 


    def champReponseOverEnter(self, event):
        #  fonction permettant de efface le texte en premier entrer
        global i
        if i == 0:  #  si c'est au premiere click 
            self.reponse.set('')  #  efface le texte
            i += 1  #  incremente le compteur 


    def champQuestionOverEnter(self, event):
        #  fonction permettant de efface le texte en premier entrer
        global j
        if j == 0:  #  si premiere click 
            self.champQuestion.delete('1.0', '1.20')   #  efface le texte
            j += 1  # incrememente le compteur 

    
    def offlinemouseOverEnter(self, event):
        """
            fonction declenché lors du survole de la souris 
                sur le menu Mode Offline dans le but d afficher le detail 
                                                                            """
        #  ci dessous creation des wigets pour afficher les details du mode survoler
        self.canvasLink = Canvas(self.root, bg ='teal', width = 251 , height = 5, bd = 0, highlightthickness = 0)
        self.canvasLink.place(relx = 0.005 , rely = 0.2275)
        self.canvasLink.create_rectangle(0, 0, 200 ,5, width = 0,  fill = 'yellow', outline = 'yellow')

        self.canvasInfo = Canvas(self.root, bg ='teal', width = 1000, height = 375)
        self.canvasInfo.place(relx = 0.07, rely = 0.27)

        self.canvasInfo.create_text(500, 20, text = 'Jouer les questions en Mode Oflline? ', font = self.arialinfo0, fill = 'yellow')
        self.canvasInfo.create_text(150, 75, text = " ◊ Unique Ordinateur utilisé ◊ ", font = self.arialinfo, fill = 'white')
        self.canvasInfo.create_text(500, 325, text = " ◊ Incrementation manuel des scores ◊ ", font = self.arialinfo, fill = 'white')
        self.canvasInfo.create_text(850, 75, text = " ◊ Aucun ressource reseau ◊ ", font = self.arialinfo, fill = 'white')
        self.offline = self.offline0.subsample(6,6)
        self.canvasInfo.create_image(500, 175, image =self.offline )


    def offlinemouseOverLeave(self, event):
        """
            fonction declancher au cas ou la souris 
                ne survole plus le mode de jeu survolé 
                                                        """
        #  tous detruire 
        self.canvasInfo.destroy()
        self.canvasLink.destroy()


    def offlineCommand(self):
        """
            fonction declenché par le bouton mode de jeu 
                pour afficher la fenetre suite 
                                                """
        self.count += 1  #  incremeneter le compteur 

        if self.count <= 1:  #  si la fenetre n'est pas ouvert 
            self.fen_f1 = Toplevel(self.root)  #  creation d une fenetr fille 
            self.fen_f1.title('QPC SESAME')
            self.fen_f1.geometry('400x100')
            self.projet = self.projet0.subsample(6, 6)
            projetImage = Label(self.fen_f1, image = self.projet).place(relx = 0.35, rely = 0.10)
            # Mise en place des boutons 
            newButton = Button(self.fen_f1, text = 'Nouveau Projet', activeforeground ='teal', command = self.newProject)
            newButton.place(relx = 0.05, rely = 0.45)
            openButton = Button(self.fen_f1, text = 'Ouvrir un Projet', activeforeground ='#032f62', command = self.openProject).place(relx = 0.65, rely = 0.45)
            self.fen_f1.protocol("WM_DELETE_WINDOW", self.fen_f1Close)  #  evenement en cas de fermeture 
            self.fen_f1.mainloop()

        else:  #  si elle est deja ouvert 
            self.fen_f1.withdraw()  #  cache la fenetre 
            self.fen_f1.deiconify()  #  reaffiche la fenetre


#  *********************************************************************************************************************************
    
    def poussoirCommand(self):
        """
        fen.root.destroy()
        fen2 = InterPoussoir()
        fen2.menuTop()
        fen2.__final__()
        """

    
    def reseauCommand(self):
        """
        fen.root.destroy()
        fen3 = InterReseau()
        fen3.__final__()
        """

    
    def __final__(self):
        self.root.mainloop()  #  lancement de la fenetre


class InterOflline(InterJeu):
    """
        classe permettant de traiter la fenetre principal du mode de jeu en Offline 
                                                                                    """ 
    def __init__(self):
        InterJeu.__init__(self)   #   appel des propriétés de la classe parent 
        self.root.title('QPC SESAME: MODE HORS LIGNE')
        global dictionnaire
        self.dict = dictionnaire
        self.validConfiguration = 0
        self.player_score = {}
        self.equipe = {}
        self.player = {}
        self.color = {}
        self.permission = False
        self.sous_partie = False
        self.dejaQues1 = [0]
        self.dejaQues2 = [0]
        self.dejaQues3 = [0]
        self.total1 = len(dictionnaire['Question1'])
        self.total2 = len(dictionnaire['Question2'])  
        self.total3 = len(dictionnaire['Question3'])
        self.incrTyp1 = 0
        self.incrTyp2 = 0
        self.incrTyp3 = 0
        self.nbrQues = 0


    def font_image(self):
        self.arialinfo14 = tkFont.Font(family='Arial', size=14)
        self.arialinfo28 = tkFont.Font(family='MS Serif', size=28, weight = 'bold')
        self.timesNew = tkFont.Font(family='Times New Rowan', size=20)
        self.groupIm = PhotoImage(file='Images\icones.png')
        self.timesNew1 = tkFont.Font(family='Times New Rowan', size=20,  slant='italic')
        
    def trierdict(self, dico):
        #  sorted(dico.items(), key=lambda t: t[1])
        return {k:v for k,v in sorted(dico.items(), key=lambda kv: kv[1])}

    def misenplace(self, refdic, dico):
        newdic = {}
        for x in refdic.keys():
            for i,j in dico.items():
                if i == x:
                    newdic[x] = j
        return newdic


    def configuration(self):
        self.config1 = Toplevel(self.root)
        self.config1.geometry('300x600+500+75')
        

    def menuTop(self):
        """
            focntion permettant de realiser des menu en haut 
                                                            """
        self.menubutton = Menu(self.root) 
        self.sous_menubutton_1 = Menu(self.menubutton, tearoff =0)  
        self.sous_menubutton_2 = Menu(self.menubutton, tearoff = 0)
        self.sous_menubutton_3 = Menu(self.menubutton, tearoff = 0)
        self.menubutton.add_cascade(label = "Fichier"  , menu = self.sous_menubutton_1)
        self.menubutton.add_cascade(label = "Edition"  , menu = self.sous_menubutton_2)
        self.menubutton.add_cascade(label = "Aide"  , menu = self.sous_menubutton_3)

        self.sous_menubutton_1.add_command(label ="Ouvrir un autre projet", command = self.reOpenProject)
        self.sous_menubutton_1.add_command(label ="Menu Principal", command = self.retour)
        self.sous_menubutton_1.add_command(label ="Quitter", command = self.confirmQuitter)

        self.sous_menubutton_2.add_command(label ="Afficher la Réponse", command = lambda: self.fenRep.deiconify())
        self.sous_menubutton_2.add_command(label ="Changer nom d'equipe")

        self.sous_menubutton_3.add_command(label ="Documentation")
        self.sous_menubutton_3.add_command(label ="Afficher la license")
        self.sous_menubutton_3.add_command(label ="A propos Developpeur")
        self.sous_menubutton_3.add_command(label ="A propos du logiciel")
        self.root.config(menu = self.menubutton)


    def reOpenProject(self):
        self.file = moduleQPC.recupfichier(extension = 'qpc')  #  ouverture de l explorer
        if self.file is not '':  #  si un fichier a ete selectionner
            f = open(self.file, 'r', encoding = 'utf8')  #  ouvrir en mode lecture seule
            try:
                self.dict = json.load(f)  #  transform en dictionnaire les données 
            except:  #  si erreur , fichier corrompu ou pas valide 
                tkmsg.showwarning('Fichier non valide', 'Attention, veuillez selectionner le bon fichier...\n Le fichier est peut être endommagé')
                self.root.withdraw()  #  cache la fenetre principale
                self.root.deiconify()  #  reafficher la fenetre 
            else:  #  si tous c est bien passé 
                self.root.quit()  #  quitter  l interface
                self.root.destroy()  #  assurer sa destruction 
                global dictionnaire  #  atteindre la variable global
                dictionnaire = self.dict   #  assigner les données
                self.root.quit()
                offlineStart()  #  lancer l interface de jeu
        else:   #  cas d une annulation
            #  rendre en premier plan la fenetre
            self.root.withdraw()
            self.root.deiconify()



    def __corps__(self):
        """
            ceci est une fonction contenant les widget principale 
                                                                    """
        #  creation du topnav du haut 
        self.nav = Canvas(self.root, bd = 4, highlightthickness = 1, bg = 'teal', width = 1380, height = 25)
        self.nav.place(relx = -0.01, rely = 0)
        #  creation d une cadre pour mettre la configuration
        self.cadre = Frame(self.root, width = 400 , height = 600, bg = 'lightgray', relief = 'ridge')
        self.cadre.place(relx = 0.35, rely = 0.1)
        #  ci dessous pour mettre un petit top avec un text 
        self.cadre_nav = Canvas(self.cadre, width = 400, height = 30, bg = 'teal', bd = 0, highlightthickness = 0)
        self.cadre_nav.create_text(200, 15, text = 'Configuration du Jeu', fill = 'Yellow', font = self.arialinfo14)
        self.cadre_nav.place(relx = 0, rely = 0)
        """ ci dessous pour les textes et les entrées """
        #  ci dessous des variables dans pour recuperer valeur 
        self.nombre_joueur = IntVar()
        self.nbrEl = IntVar()  #  nombre d'equipe d'eliminé par manche
        self.nbrLimite = IntVar()  #  variable d'arret de jeu
        self.nbrLimite.set(20)
        #  ci dessus la creation des widgets
        text1 = Label(self.cadre, text = "Nombre d'equipe: ", font = self.arialinfo14, bg = 'lightgray')
        text1.place(relx = 0.048, rely = 0.1)
        text1.bind_all('<Any-KeyPress>', self.vrfnbr)
        self.entre1 = Entry(self.cadre, textvariable = self.nombre_joueur, font = self.arialinfo14, width = 30)
        self.entre1.place(relx = 0.05, rely = 0.15)
        text2 = Label(self.cadre, text = "Nombre d'equipe eliminé par manche: ", font = self.arialinfo14, bg = 'lightgray')
        text2.place(relx = 0.048, rely = 0.25)
        self.entre2 = Entry(self.cadre, textvariable = self.nbrEl, font = self.arialinfo14, width = 30)
        self.entre2.place(relx = 0.05, rely = 0.3)
        #  ci dessous un radioboutton 
        text3 = Label(self.cadre, text = "Limitation d'une manche par nombre de: ", font = self.arialinfo14, bg ='lightgray')
        text3.place(relx = 0.048, rely = 0.4)
        self.etiquette = ['Points', 'Question']
        self.choix = IntVar()
        for i in range(2):  #  positionnement du radio 
            self.RadioChoix = Radiobutton(self.cadre, variable = self.choix, text = self.etiquette[i], value = i, font = self.arialinfo14, bg ='lightgray', command = self.changeValue)
            self.RadioChoix.place(relx = 0.05+(0.5*i), rely = 0.45)
        #  variable d'arret de jeu 
        entre3 = Entry(self.cadre, textvariable = self.nbrLimite, font = self.arialinfo14, width = 15) 
        entre3.place(relx = 0.05 , rely = 0.52)
        self.entre3_comp = Label(self.cadre, text = ' points', font = self.arialinfo14)
        self.entre3_comp.place(relx = 0.5, rely = 0.52)
        #  mode d'affichage des questions
        self.options = StringVar()
        self.options.set("Choisir le type d'affichage des questions")
        options = ('1) Niveau Aléatoire  - Question aléatoire', '2) Niveau Manuel - Question aléatoire', '3) Niveau Aléatoire et Question en ordre', '4) Niveau Manuel - Question en ordre')
        self.slist = OptionMenu(self.cadre, self.options, *options)
        self.slist.config(font=self.arialinfo14)
        self.slist.place(relx=0.02, rely=0.6)
        #  confirmation de suite
        self.configurer_nom = Button(self.cadre, text ="Personaliser nom d'equipe", font = self.arialinfo14, command = self.configurationNom)
        self.configurer_nom.place(relx = 0.2, rely = 0.75)
        self.suivant = Button(self.cadre, text = 'COMMENCER', fg ='yellow', bg ='teal', font = self.arialinfo14, command = self.gamestart)
        self.suivant.place(relx = 0.3, rely= 0.85)
        self.info = Label(self.cadre, text ='', fg = 'red')
        self.info.place(relx = 0.2, rely = 0.95)


    def vrfnbr(self, event):
        if self.nombre_joueur.get() < 0:
            self.nombre_joueur.set(self.nombre_joueur.get()*(-1))
        if self.nombre_joueur.get() > 12:
            self.nombre_joueur.set(12)
        

    def configurationNom(self):
        self.validConfiguration += 1
        config = Toplevel(self.root)
        spc = 5

        if self.nombre_joueur.get() > 10:
            spc = 1

        for i in range(self.nombre_joueur.get()):
            self.equipe[f'player{i+1}'] = StringVar()
            self.color[f'player{i+1}'] = 'teal'
            label = Label(config, text = f'Nom equipe {i+1}').pack(pady = {spc})
            entry = Entry(config, textvariable = self.equipe[f'player{i+1}']).pack()
            

        but = Button(config, text = 'Valider', command = config.destroy).pack(pady=10)
          

    def changeValue(self):
        if self.choix.get() == 0:
            self.entre3_comp.config(text = ' points')
        elif self.choix.get() == 1:
            self.entre3_comp.config(text = 'questions')

        self.entre3_comp.update()
    

    def retour(self):
        self.root.destroy()
        fen = Interface() 
        fen.__corps__()
        fen.__final__()

        
    def confirmQuitter(self):
        self.fermer = tkmsg.askquestion("Confirmer la fermeture!", "Voulez-vous vraiment quitter?")
        if self.fermer == "yes":
            self.root.quit()
            self.root.destroy()


    def gamestart(self):
        try:
            int(self.options.get()[0])
            self.info.config(text='')
            self.info.update()
            if self.validConfiguration > 0:
                if self.nombre_joueur.get() >= 2:
                    self.cadre.destroy()
                    self.cadre_question = Frame(self.root, width = 600 , height = 350, bg = 'lightgray', relief = 'ridge')
                    self.cadre_question.place(relx = 0.2, rely = 0.25)

                    self.Label_Question = Label(self.cadre_question, text = "QUESTION", font = self.arialinfo28, fg = 'teal').place(relx=0.3, rely=0.05)

                    self.Label_Champ = Text(self.cadre_question, width = 37, height = 8, bg = 'teal', fg = 'yellow', font=self.timesNew)
                    self.Label_Champ.place(relx = 0.03, rely = 0.2)
                    self.typeQuestion = int(self.options.get()[0])

                    self.launched()
                    self.permission = True
                    self.cadre_score()
                    self.jeu_suivant(debut=True)     

                else:
                    self.info.config(text=f'Nombre de joueur entrée: {self.nombre_joueur.get()} invalide')
                    self.info.update()
                    self.validConfiguration = 0

            else:
                self.info.config(text=f"Veuiller d'abord personaliser le nom d'equipe")
                self.info.update()
                self.validConfiguration = 0
        except:
            self.info.config(text="Veuiller choisir le type d'affichage des questions")
            self.info.update()
            
        

    def cadre_score(self):
        if self.permission:
            try:
                self.cadreScore.destroy()
            except:
                pass

            self.cadreScore = Frame(self.root, width = 250, height = 685, bg ='lightgray', highlightthickness = 0)
            self.cadreScore.grid_propagate(0)
            self.cadreScore.place(relx=0.82, rely=0.047)

            for i in range(self.nombre_joueur.get()): 
                self.player_score = self.trierdict(self.player_score)
                self.equipe = self.misenplace(self.player_score, self.equipe)
                self.color = self.misenplace(self.player_score, self.color)

                self.playerAf = Canvas(self.cadreScore, width=250, height=50, bg = list(self.color.values())[::-1][i], highlightthickness = 0)
                self.playerAf.create_text(125, 15, text = list(self.equipe.values())[::-1][i].get(), font = self.arialinfo14, fill ='yellow')
                self.playerAf.create_text(125, 35, text = str(list(self.player_score.values())[::-1][i]) + ' points', fill = 'black')
                self.playerAf.pack(pady=3)
                self.playerAf.create_text(25, 25, text = str(i+1), font = self.arialinfo28, fill = 'yellow')
            
        self.permission = False


    def incrementer(self, player):
        authorize = True

        if self.sous_partie:
            if self.player_score[player] < self.nbrLimite.get():
                self.player_score[player]+=self.textPoint
                self.cadre_score()
                count = 0
                for x in self.player_score.values():
                    if x < self.nbrLimite.get():  #  n nombre de personne non qualifié
                        count += 1

                if self.ilaina == count: 
                    self.jeu_suivant(sousfin=True)
                else:
                    self.jeu_suivant(milieu=True)

                self.points.destroy()
            
            authorize = False

            
        if self.permission and authorize:
            self.player_score[player]+=self.textPoint
            self.cadre_score()
            if self.choix.get() == 0:  #  0 est attribué aux Points
                if self.player_score[player] >= self.nbrLimite.get():
                    self.jeu_suivant(fin=True)
                else:
                    self.jeu_suivant(milieu=True)
            else:  #  nombre de questions
                if self.nbrQues >= self.nbrLimite.get():
                    self.jeu_suivant(fin=True)
                else:
                    self.jeu_suivant(milieu=True)

            self.points.destroy()


    def launched(self):
        for i in range(self.nombre_joueur.get()):
            self.player_score[f'player{i+1}'] = 0

            if self.equipe[f'player{i+1}'].get() == '':
                self.equipe[f'player{i+1}'].set(f'Joueur{i+1}')

            self.player[f"player{i+1}"] = Canvas(self.root, width = 150, height = 100)
            self.player[f"player{i+1}"].create_image(75, 50, image = self.groupIm)
            self.player[f"player{i+1}"].create_text(75, 85, text = self.equipe[f'player{i+1}'].get(), font = self.arialinfo14)

        if (self.nombre_joueur.get() <= 4):
            self.player['player1'].bind('<Button-1>', lambda f: self.incrementer('player1'))
            self.player['player1'].place(relx = 0.07, rely = 0.4)
            self.player['player2'].bind('<Button-1>', lambda f: self.incrementer('player2'))
            self.player['player2'].place(relx = 0.67, rely = 0.4)
            if (self.nombre_joueur.get() >= 3):
                self.player['player3'].place(relx = 0.35, rely = 0.77)
                self.player['player3'].bind('<Button-1>', lambda f: self.incrementer('player3'))
                if (self.nombre_joueur.get() == 4):
                    self.player['player4'].bind('<Button-1>', lambda f: self.incrementer('player4'))
                    self.player['player4'].place(relx=0.35, rely=0.07)

        elif (self.nombre_joueur.get() == 5):
            self.player['player1'].bind('<Button-1>', lambda f: self.incrementer('player1'))
            self.player['player2'].bind('<Button-1>', lambda f: self.incrementer('player2'))
            self.player['player3'].bind('<Button-1>', lambda f: self.incrementer('player3'))
            self.player['player4'].bind('<Button-1>', lambda f: self.incrementer('player4'))
            self.player['player5'].bind('<Button-1>', lambda f: self.incrementer('player5'))
            self.player['player1'].place(relx = 0.06, rely = 0.4)
            self.player['player3'].place(relx = 0.67, rely = 0.4)
            self.player['player2'].place(relx = 0.35, rely = 0.77)
            self.player['player5'].place(relx = 0.22, rely=0.07)
            self.player['player4'].place(relx = 0.5, rely=0.07)

        elif (self.nombre_joueur.get() == 6):
            self.player['player1'].bind('<Button-1>', lambda f: self.incrementer('player1'))
            self.player['player2'].bind('<Button-1>', lambda f: self.incrementer('player2'))
            self.player['player3'].bind('<Button-1>', lambda f: self.incrementer('player3'))
            self.player['player4'].bind('<Button-1>', lambda f: self.incrementer('player4'))
            self.player['player5'].bind('<Button-1>', lambda f: self.incrementer('player5'))
            self.player['player6'].bind('<Button-1>', lambda f: self.incrementer('player6'))
            self.player['player1'].place(relx = 0.07, rely = 0.4)
            self.player['player4'].place(relx = 0.67, rely = 0.4)
            self.player['player2'].place(relx = 0.22, rely = 0.77)
            self.player['player3'].place(relx = 0.5, rely = 0.77)
            self.player['player6'].place(relx = 0.22, rely=0.07)
            self.player['player5'].place(relx = 0.5, rely=0.07)

        elif (self.nombre_joueur.get() == 7):
            self.player['player1'].bind('<Button-1>', lambda f: self.incrementer('player1'))
            self.player['player2'].bind('<Button-1>', lambda f: self.incrementer('player2'))
            self.player['player3'].bind('<Button-1>', lambda f: self.incrementer('player3'))
            self.player['player4'].bind('<Button-1>', lambda f: self.incrementer('player4'))
            self.player['player5'].bind('<Button-1>', lambda f: self.incrementer('player5'))
            self.player['player6'].bind('<Button-1>', lambda f: self.incrementer('player6'))
            self.player['player7'].bind('<Button-1>', lambda f: self.incrementer('player7'))
            self.player['player1'].place(relx = 0.07, rely = 0.4)
            self.player['player4'].place(relx = 0.67, rely = 0.55)
            self.player['player5'].place(relx = 0.67, rely = 0.27)
            self.player['player2'].place(relx = 0.22, rely = 0.77)
            self.player['player3'].place(relx = 0.5, rely = 0.77)
            self.player['player7'].place(relx = 0.22, rely=0.07)
            self.player['player6'].place(relx = 0.5, rely=0.07)

        elif (self.nombre_joueur.get() == 8):
            self.player['player1'].bind('<Button-1>', lambda f: self.incrementer('player1'))
            self.player['player2'].bind('<Button-1>', lambda f: self.incrementer('player2'))
            self.player['player3'].bind('<Button-1>', lambda f: self.incrementer('player3'))
            self.player['player4'].bind('<Button-1>', lambda f: self.incrementer('player4'))
            self.player['player5'].bind('<Button-1>', lambda f: self.incrementer('player5'))
            self.player['player6'].bind('<Button-1>', lambda f: self.incrementer('player6'))
            self.player['player7'].bind('<Button-1>', lambda f: self.incrementer('player7'))
            self.player['player8'].bind('<Button-1>', lambda f: self.incrementer('player8'))
            self.player['player1'].place(relx = 0.07, rely = 0.27)
            self.player['player2'].place(relx = 0.07, rely = 0.55)
            self.player['player5'].place(relx = 0.67, rely = 0.55)
            self.player['player6'].place(relx = 0.67, rely = 0.27)
            self.player['player3'].place(relx = 0.22, rely = 0.77)
            self.player['player4'].place(relx = 0.5, rely = 0.77)
            self.player['player8'].place(relx = 0.22, rely=0.07)
            self.player['player7'].place(relx = 0.5, rely=0.07)

        elif (self.nombre_joueur.get() <= 12):
            self.player['player1'].bind('<Button-1>', lambda f: self.incrementer('player1'))
            self.player['player2'].bind('<Button-1>', lambda f: self.incrementer('player2'))
            self.player['player3'].bind('<Button-1>', lambda f: self.incrementer('player3'))
            self.player['player4'].bind('<Button-1>', lambda f: self.incrementer('player4'))
            self.player['player5'].bind('<Button-1>', lambda f: self.incrementer('player5'))
            self.player['player6'].bind('<Button-1>', lambda f: self.incrementer('player6'))
            self.player['player7'].bind('<Button-1>', lambda f: self.incrementer('player7'))
            self.player['player8'].bind('<Button-1>', lambda f: self.incrementer('player8'))
            self.player['player1'].place(relx = 0.05, rely = 0.2)
            self.player['player2'].place(relx = 0.05, rely = 0.62)
            self.player['player5'].place(relx = 0.67, rely = 0.62)
            self.player['player6'].place(relx = 0.67, rely = 0.2)
            self.player['player3'].place(relx = 0.2, rely = 0.77)
            self.player['player4'].place(relx = 0.52, rely = 0.77)
            self.player['player8'].place(relx = 0.2, rely=0.07)
            self.player['player7'].place(relx = 0.52, rely=0.07)

            if self.nombre_joueur.get() >= 9:
                self.player['player9'].bind('<Button-1>', lambda f: self.incrementer('player9'))
                self.player['player9'].place(relx = 0.04, rely = 0.4)

            if self.nombre_joueur.get() >= 10:
                self.player['player10'].bind('<Button-1>', lambda f: self.incrementer('player10'))
                self.player['player10'].place(relx = 0.36, rely = 0.77)

            if self.nombre_joueur.get() >= 11:
                self.player['player11'].bind('<Button-1>', lambda f: self.incrementer('player11'))
                self.player['player11'].place(relx = 0.68, rely = 0.4)

            if self.nombre_joueur.get() == 12:
                self.player['player12'].bind('<Button-1>', lambda f: self.incrementer('player12'))
                self.player['player12'].place(relx = 0.36, rely = 0.07)

        
    def jeu_suivant(self, debut=False, milieu=False, fin=False, sousfin=False, terminer=False):
        self.Label_Champ.delete('1.0','10.0')
        if debut:
            self.bt_Start = Button(self.cadre_question, text='COMMENCER', font=self.timesNew1, bg ='yellow', command=self.lancer_jeu)
            self.bt_Start.place(relx=0.3, rely=0.4)

        if milieu:
            self.bt_Start = Button(self.cadre_question, text='Question Suivante', font=self.timesNew1, bg ='yellow', command=self.lancer_jeu)
            self.bt_Start.place(relx=0.27, rely=0.4)

        if fin:
            el = 0
            score = list(self.player_score.values()).copy()
            score.append('')
            mov = ''
            elList = []
            sous = False
            while el != self.nbrEl.get():  #  nbrEl etant le nbr eliminé par manche
                try:
                 while True:
                    score.remove(mov)
                except:
                    pass
                minV = min(score)
                cntV = score.count(minV)

                if cntV == 1:
                    mov = minV
                    el += 1
                    elList.append(minV)

                elif cntV == self.nbrEl.get() and elList == []:
                    elList.append(minV)
                    break

                elif cntV > 1 and cntV < self.nbrEl.get():
                    if (el + cntV) == self.nbrEl.get():
                        el = self.nbrEl.get()
                        elList.append(minV)
                        mov = minV
                    elif (el + cntV) < self.nbrEl.get():
                        el += cntV
                        elList.append(minV)
                        mov = minV
                    elif (el + cntV) > self.nbrEl.get():
                        sous = True
                        break
                
                elif cntV > 1 and cntV >= self.nbrEl.get():
                    sous = True
                    break

            for k,v in self.player_score.items():
                if v in elList:
                    self.color[k] = 'red'

            if sous:
                for k,v in self.player_score.items():
                    if v == minV:
                        self.color[k] = 'orange'


            self.permission = True
            self.cadre_score()

            self.root['bg'] ='green'
            if sous:
                self.bt_Start = Button(self.cadre_question, text='Commencer Sous-Partie', font=self.timesNew1, bg ='yellow', command=self.sousPartie)
                self.bt_Start.place(relx=0.2, rely=0.4)
            else:
                self.bt_Start = Button(self.cadre_question, text='Manche Suivante', font=self.timesNew1, bg ='yellow', command = self.mancheSuiv)
                self.bt_Start.place(relx=0.27, rely=0.4)
            
        if sousfin:
            for k,v in self.player_score.items():
                if v < self.nbrLimite.get():
                    self.color[k] = 'red'
            self.permission = True
            self.cadre_score()
            self.nbrLimite.set(self.nbrLimiteSave)
            self.choix.set(self.choixSave)
        
            self.equipeNew = {}
            j = 0
            for k,v in self.colorSave.items():
                if v == 'teal':
                    j += 1
                    self.equipeNew[f'player{j}'] = self.equipeSave[k]
            for k,v in self.color.items():
                if v == 'teal':
                    j += 1
                    self.equipeNew[f'player{j}'] = self.equipe[k]

            self.equipe = self.equipeNew
            self.nombre_joueur.set(len(self.equipe))
            self.color.clear()
            for i in range(self.nombre_joueur.get()):
                self.color[f'player{i+1}'] = 'teal'

            self.sous_partie = False
            self.root['bg'] = 'green'
            try:
                self.bt_Start.destroy()
            finally:
                self.bt_Start = Button(self.cadre_question, text='Manche Suivante', font=self.timesNew1, bg ='yellow', command=self.sousLancer)
                self.bt_Start.place(relx=0.27, rely=0.4)
            self.nbrQues = 0


        if terminer:
            pass

    def sousLancer(self):
        for k,v  in self.player.items():
            v.destroy()
        self.player.clear()
        self.bt_Start.destroy()
        self.root['bg'] = 'white'
        self.launched()
        self.permission = True
        self.cadre_score()
        self.jeu_suivant(debut=True) 



    def randomQues(self, niveau, simulation=False):
        if niveau == 1:
            i = 0
            while i in self.dejaQues1:
                if list(x for x in range(self.total1+1)) == list(set(self.dejaQues1)):
                    return 0
                i = random.randint(1, self.total1)
            if simulation == False:
                self.dejaQues1.append(i)

        elif niveau == 2:
            i = 0
            while i in self.dejaQues2:
                if list(x for x in range(self.total2+1)) == list(set(self.dejaQues2)):
                    return 0
                i = random.randint(1, self.total2)
            if simulation == False:
                self.dejaQues2.append(i)

        elif niveau == 3:
            i = 0
            while i in self.dejaQues3:
                if list(x for x in range(self.total3+1)) == list(set(self.dejaQues3)):
                    return 0
                i = random.randint(1, self.total3)
            if  simulation == False:
                self.dejaQues3.append(i)
        
        return i

    
    def choisirNiv(self, res=False, quat=False):
        self.permission = False
        self.choisirFen = Toplevel(self.root)
        self.choisirFen.geometry('400x150+375+250')
        self.choisirFen.title('Choisir Niveau')
        Label(self.choisirFen, text = 'Niveau de question', font = self.arialinfo14).pack()
        etiquette = ['Niveau 1', 'Niveau 2', 'Niveau 3']
        values = [1 , 2 , 3]  # ses valeurs initial selon l ordre du nom 
        self.choixNiveau = IntVar()  #  variable qui va recuperer le choix 
        for i in range(3):  #  positionnement du radio 
            Rniveau = Radiobutton(self.choisirFen, variable = self.choixNiveau, text = etiquette[i], value = values[i], font = self.arialinfo14)
            Rniveau.place(relx =(0.05+(i*0.31)), rely = 0.4)
        if quat:
             Button(self.choisirFen, text = 'Selectionner', font= self.arialinfo14, command = lambda: self.ordQues(self.choixNiveau.get())).place(relx = 0.33, rely = 0.7)
        else:
            Button(self.choisirFen, text = 'Selectionner', font= self.arialinfo14, command = lambda: self.afficherQuesPoint(self.choixNiveau.get(), True)).place(relx = 0.33, rely = 0.7)

        
    def ordQues(self, niv):
        self.permission = True
        self.choisirFen.destroy()
        if niv == 1:
            self.incrTyp1 += 1
            if self.incrTyp1 <= self.total1:
                number = self.incrTyp1
            else:
                number = 0
                tkmsg.showwarning('Question Niveau 1', 'Attention, il y a plus de question dans ce Niveau')
        elif niv == 2:
            self.incrTyp2 += 1
            if self.incrTyp2 <= self.total2:
                number = self.incrTyp2
            else:
                number = 0
                tkmsg.showwarning('Question Niveau 1', 'Attention, il y a plus de question dans ce Niveau')
        elif niv == 3:
            self.incrTyp3 += 1
            if self.incrTyp3 <= self.total3:
                number = self.incrTyp3
            else:
                number = 0
                tkmsg.showwarning('Question Niveau 1', 'Attention, il y a plus de question dans ce Niveau')

        if number != 0:
            question = dictionnaire[f'Question{niv}'][number - 1][0]
            self.textPoint = dictionnaire[f'Reponse{niv}'][number - 1][1]
            self.devoiRep(dictionnaire[f'Reponse{niv}'][number - 1][0])

            self.points = Label(self.cadre_question, text = f'{self.textPoint} points', font=self.arialinfo14, fg='red')
            self.points.place(relx = 0.82, rely = 0.1)

            self.inserQues(question)

        else:
            self.permission = False
            self.Label_Champ.delete('1.0', '10.0')
            if (self.incrTyp1 <= self.total1) or (self.incrTyp2 <= self.total2) or (self.incrTyp3 <= self.total3):
                self.lancer_jeu()
            else:
                self.Label_Champ.insert('1.0', "Il n'y a plus de question.")


    def lancer_jeu(self):
        self.permission = True
        i = 0
        self.bt_Start.destroy()
        global dictionnaire

        if self.typeQuestion == 1:
            nivs = []
            nivs0 = []
            niv = random.randint(1, 3)
            test = self.randomQues(niveau=niv, simulation=True)
            while test == 0:
                nivs.append(niv)
                niv = random.randint(1, 3)
                if niv not in nivs:
                    test = self.randomQues(niveau=niv, simulation=True)
                if test == 0:
                    nivs0.append(niv)
                if [1, 2, 3] == list(set(nivs0)):
                    niv = 0
                    break
            if niv == 0:
                self.Label_Champ.delete('1.0', '10.0')
                self.Label_Champ.insert('1.0', "Il n'y a plus de question.")
                self.permission = False
            else:
                self.afficherQuesPoint(niv)

        elif self.typeQuestion == 2:
            self.choisirNiv()

        elif self.typeQuestion == 3:
            niv = random.randint(1, 3)
            if niv == 1:
                self.incrTyp1 += 1
                if self.incrTyp1 <= self.total1:
                    number = self.incrTyp1
                else:
                    number = 0
            elif niv == 2:
                self.incrTyp2 += 1
                if self.incrTyp2 <= self.total2:
                    number = self.incrTyp2
                else:
                    number = 0
            elif niv == 3:
                self.incrTyp3 += 1
                if self.incrTyp3 <= self.total3:
                    number = self.incrTyp3
                else:
                    number = 0

            if number != 0:
                question = dictionnaire[f'Question{niv}'][number - 1][0]
                self.textPoint = dictionnaire[f'Reponse{niv}'][number - 1][1]
                self.devoiRep(dictionnaire[f'Reponse{niv}'][number - 1][0])

                self.points = Label(self.cadre_question, text = f'{self.textPoint} points', font=self.arialinfo14, fg='red')
                self.points.place(relx = 0.82, rely = 0.1)

                self.inserQues(question)
            else:
                self.permission = False
                self.Label_Champ.delete('1.0', '10.0')
                if (self.incrTyp1 <= self.total1) or (self.incrTyp2 <= self.total2) or (self.incrTyp3 <= self.total3):
                    self.lancer_jeu()
                else:
                    self.Label_Champ.insert('1.0', "Il n'y a plus de question.")

        elif self.typeQuestion == 4:
            self.choisirNiv(quat=True)
        
    
    def afficherQuesPoint(self, niv, sec=False):
        self.permission = True
        number = self.randomQues(niv)
        autorise = True
        if sec:
            if number == 0:
                autorise = False
            else:
                self.choisirFen.destroy()
        if autorise:
            global dictionnaire
            question = dictionnaire[f'Question{niv}'][number - 1][0]
            self.textPoint = dictionnaire[f'Reponse{niv}'][number - 1][1]
            self.devoiRep(dictionnaire[f'Reponse{niv}'][number - 1][0])

            self.points = Label(self.cadre_question, text = f'{self.textPoint} points', font=self.arialinfo14, fg='red')
            self.points.place(relx = 0.82, rely = 0.1)

            self.inserQues(question)
        else:
            self.Lab_vide = Label(self.choisirFen, text = f"Il n'y as pas plus de question dans le niveau {niv}", fg ='red')
            self.Lab_vide.place(relx = 0.2, rely = 0.3)


    def devoiRep(self, reponse):
        try:
            self.fenRep.destroy()
        except:
            pass
        finally:
            self.fenRep = Toplevel(self.root)
            self.fenRep.title('Reponse...')
            self.fenRep.geometry('300x50')
            self.LabRepone = Label(self.fenRep, text = reponse)
            self.bt_devoiler = Button(self.fenRep, text = 'AFFICHER', command=self.aff_devoiRep)
            self.bt_devoiler.pack()
            self.fenRep.withdraw()
    
    def aff_devoiRep(self):
        self.bt_devoiler.destroy()
        self.LabRepone.pack()

    
    def inserQues(self, question):
        self.Label_Champ.insert('1.0', question)
        self.nbrQues += 1


    def mancheSuiv(self):
        self.nbrQues = 0
        self.root['bg'] = 'white'
        self.cadreScore.destroy()
        c = 0
        for k,v in self.color.items():
            if v != 'red':
                c += 1
            else:
                self.equipe.pop(k)
        
        self.nombre_joueur.set(c)
        val = list(self.equipe.values())
        self.equipe.clear()
        self.color.clear()
        for i in range(self.nombre_joueur.get()):
            self.equipe[f'player{i+1}'] = val[i]
            self.color[f'player{i+1}'] = 'teal'

        for k,v  in self.player.items():
            v.destroy()
        
        self.player.clear()

        self.cadre_question.destroy()
        self.cadre_question = Frame(self.root, width = 600 , height = 350, bg = 'lightgray', relief = 'ridge')
        self.cadre_question.place(relx = 0.2, rely = 0.25)

        self.Label_Question = Label(self.cadre_question, text = "QUESTION", font = self.arialinfo28, fg = 'teal').place(relx=0.3, rely=0.05)

        self.Label_Champ = Text(self.cadre_question, width = 37, height = 8, bg = 'teal', fg = 'yellow', font=self.timesNew)
        self.Label_Champ.place(relx = 0.03, rely = 0.2)
        self.typeQuestion = int(self.options.get()[0])
        self.player_score.clear()
        self.launched()
        self.permission = True
        self.cadre_score()
        self.jeu_suivant(debut=True)     


    def sousPartie(self):
        self.bt_Start.destroy()
        self.sPartFen = Toplevel(self.root)
        varP = IntVar()
        Label(self.sPartFen, text = 'Points Qualifiés').pack()
        Entry(self.sPartFen, textvariable=varP).pack(pady=10)
        Button(self.sPartFen, text = 'Commencer', font=self.arialinfo14, fg = 'red', command = lambda: self.sousPar_start(varP)).pack()


    def sousPar_start(self, nbrE):
        self.sous_partie = True
        self.sPartFen.destroy()
        self.equipeSave = self.equipe.copy()
        self.colorSave = self.color.copy()

        self.nbrQues = 0
        self.root['bg'] = 'white'
        self.cadreScore.destroy()
        c = 0
        elC = 0
        for k,v in self.color.items():
            if v != 'orange':
                if v == 'red':
                    elC += 1
                    self.equipe.pop(k)
            else:
                c += 1
                
        self.ilaina = self.nbrEl.get() - elC 
        self.nombre_joueur.set(c)
        val = list(self.equipe.values())
        self.equipe.clear()
        self.color.clear()
        for i in range(self.nombre_joueur.get()):
            self.equipe[f'player{i+1}'] = val[i]
            self.color[f'player{i+1}'] = 'teal'

        for k,v  in self.player.items():
            v.destroy()
        
        self.player.clear()
        self.choixSave = self.choix.get()
        self.nbrLimiteSave = self.nbrLimite.get()
        self.choix.set(0)
        self.nbrLimite.set(nbrE.get())

        self.cadre_question.destroy()
        self.cadre_question = Frame(self.root, width = 600 , height = 350, bg = 'lightgray', relief = 'ridge')
        self.cadre_question.place(relx = 0.2, rely = 0.25)

        self.Label_Question = Label(self.cadre_question, text = "QUESTION", font = self.arialinfo28, fg = 'teal').place(relx=0.3, rely=0.05)

        self.Label_Champ = Text(self.cadre_question, width = 37, height = 8, bg = 'teal', fg = 'yellow', font=self.timesNew)
        self.Label_Champ.place(relx = 0.03, rely = 0.2)
        self.typeQuestion = int(self.options.get()[0])
        self.player_score.clear()

        self.launched()
        self.permission = True
        self.cadre_score()
        self.jeu_suivant(debut=True) 


    def __final__(self):
        self.root.mainloop()



def offlineStart():
    """
        fonction pour demarer la fenetre du mode
            de jeu offline et de  controler son comportement
                                                                """
    fenetreOff = InterOflline()
    fenetreOff.font_image()
    fenetreOff.__corps__()
    fenetreOff.menuTop()
    fenetreOff.__final__()



if __name__ == '__main__':   
    fen = Interface()   #  lanceons now notre fenetre
    fen.__corps__()
    fen.__final__()
    
