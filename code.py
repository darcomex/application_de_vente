from tkinter import*
from time import*
import os
 
fenetre = Tk()
fenetre.title("                                                                                                                                                                                                                                         GameCorp")
fenetre.config(width=1400,height=1000,bg="#1A1A1C")
canevas = Canvas(fenetre, width=1400, height=1000,bg="#1A1A1C")
canevas.place(x=0, y=0)
#Insertion des images
DIVSION= PhotoImage(file="divison.gif")
FF7= PhotoImage(file="ff7.gif")
GHOST=PhotoImage(file='ghostee.gif')
MANETTE= PhotoImage(file="manette a palette.gif")
NBA= PhotoImage(file="nba.gif")
PS5= PhotoImage(file="ps5.gif")
SWITCHE= PhotoImage(file="switch.gif")
panier=PhotoImage(file='paniersteam.gif')
logo= PhotoImage(file="logo.gif")
cadenas= PhotoImage(file="cadena.png")
paniere= PhotoImage(file="panier.gif")
login= PhotoImage(file="profil.gif")
 
#image placer dans la fenetre principal
canevas.create_image(100,100, image=logo)
canevas.create_image(1300,100, image=login)
 
 
texte1=canevas.create_text(168,525,fill="antiquewhite",font="black",text="45.95€")
texte2=canevas.create_text(472,525,fill="antiquewhite",font="black",text="38.97€")
texte3=canevas.create_text(773,525,fill="antiquewhite",font="black",text="69.95€")
texte4=canevas.create_text(1069,525,fill="antiquewhite",font="black",text="20.95€")
texte5=canevas.create_text(195,898,fill="antiquewhite",font="black",text="49.99€")
texte6=canevas.create_text(660,896,fill="antiquewhite",font="black",text="499.99€")
texte7=canevas.create_text(995,898,fill="antiquewhite",font="black",text="310.99€")
text_princip = Label(fenetre, text='Bienvenu chez GameCorp le site ou tous vos jeux sont dispo ! \n\n Vous pouvez avoir des detail des articles en cliquant dessus', fg='#A7AE35',bg="#1A1A1C")
text_princip.config(font= ('Underline' ,19,'underline'))
text_princip.place(x=330,y=100)
#initialisation des variables
connecter = False
moove = False
final = None
ps5 = None
nba2k = None
ghost = None
manette = None
switch = None
Divison = None
paniertotal = None
bouger_la_souris = None
def Delog():
    global connecter
    if moove is False:
        connecter = False
        fenetre.title('GameCorp.dz')
def Bouger(moove):
    moove = True
    fenetre.after(60000,Delog)
def Deco():
    global moove
    moove=False
    fenetre.after(1,Deco)
fenetre.after(1,Deco)
 
#methodes cliquegauche pour acceder au login
def cliquegauche(event):
    print(event.x, event.y)
    if 1200 < event.x < 1400:
        if 0 < event.y < 200:
            login = Toplevel()
            login.title("Login")
            w=350 
            h=285 
            ws=login.winfo_screenwidth() 
            hs=login.winfo_screenheight() 
            x=(ws/1.5)-(w/1.2) 
            y=(hs/3.9)-(h/2)
            login.geometry('+%d+%d'%(x,y))
            login.config(width=600,height=300)
            canevas = Canvas(login, width=600, height=300,bg="#1A1A1C")
            canevas.place(x=0, y=0)
            canevas.create_image(440,150, image=cadenas)
            login.grab_set()
            login.transient(login.master)
            txtndc = Label(login, text='Nom de compte :', fg='red', bg="#1A1A1C")
            txtndc.config(font= ('verdana' ,8,'normal'))
            txtndc.place(x=35,y=70)
            entryndc = Entry(login)
            entryndc.place(x=140,y=70)
            txtmdp = Label(login, text='Mot de passe :', fg='red',bg="#1A1A1C")
            txtmdp.config(font= ('verdana' ,8,'normal'))
            txtmdp.place(x=45,y=100)
            entrymdp = Entry(login)
            entrymdp.place(x=140,y=100)
            def connexionuser():
                global connecter
                mon_fichier=open('log.csv','r')
                texte=mon_fichier.read()
                mon_fichier.close()
                tableau=texte.split('\n')
                ndccode = entryndc.get()
                mdpcode = entrymdp.get()
                Login = ndccode+';'+mdpcode
                print(Login)
                if Login in tableau:
                    login.destroy()
                    fenetre.title('GameCorp.dz                                                                                                                                                              session de : '+ ndccode)
                    connecter = True
                    print(connecter)
                else:
                    erreur_login = Label(login, text="Nom de compte ou mots de passe incorrect \n ou ce compte n'éxiste pas veuiller vous créer un compte", fg='red',bg="#1A1A1C")
                    erreur_login.config(font=('verdana', 8,'normal'))
                    erreur_login.place(x=5,y=150)
            #fenetre de creation de login
            def creation_account():
                creationuser = Toplevel()
                creationuser.title("Creation du login")
                w=350 
                h=285 
                ws=creationuser.winfo_screenwidth() 
                hs=creationuser.winfo_screenheight() 
                x=(ws/1.2)-(w/1.2) 
                y=(hs/3.9)-(h/2)
                creationuser.geometry('+%d+%d'%(x,y)) 
                creationuser.config(width=400,height=250)
                canevas = Canvas(creationuser, width=400, height=250,bg="#1A1A1C")
                canevas.place(x=0, y=0)
                creationuser.grab_set()
                creationuser.transient(login.master)
                def creer_le_compte():
                    mon_fichier=open('log.csv','r')
                    texte=mon_fichier.read()
                    mon_fichier.close()
                    tableau=texte.split('\n')
                    ndccode = creer_entry_utilisateur.get()
                    mdpcode = creer_entry_mot_de_passe.get()
                    entree_conf_mot_de_passe = conf_entry_mot_de_passe.get()
                    if ndccode+';'+mdpcode in tableau:
                        erreur_identifiant = Label(creationuser, text="L'identifiant est déjà utiliser",fg='red',bg='#1A1A1C')
                        erreur_identifiant.config(font= ('verdana' ,12,'normal'))
                        erreur_identifiant.place(x=5,y=170)
                    else:
                        if mdpcode == entree_conf_mot_de_passe:
                            good_login = Label(creationuser, text='Compte bien enregistrer \n vous pouvez cliquer sur retour',fg='red',bg='#1A1A1C')
                            good_login.config(font= ('verdana' ,12,'normal'))
                            good_login.place(x=5,y=170)
                            nombre_ligne=len(tableau)
                            tableau.insert(nombre_ligne,ndccode+';'+mdpcode)
                            nombre_ligne=len(tableau)
                            for i in range(nombre_ligne):
                                mon_fichier=open('log.csv','w')
                                mon_fichier.write(texte+'\n'+tableau[i])
                                mon_fichier.close()
                            creationuser.destroy()
                        else:
                            erreur_mot_de_passe = Label(creationuser, text='Le mot de passe ne \n correspond pas',fg='red',bg='#1A1A1C')
                            erreur_mot_de_passe.config(font= ('verdana' ,12,'normal'))
                            erreur_mot_de_passe.place(x=5,y=170)
                #Identifiant
                creer_utilisateur = Label(creationuser, text='Identifiant :',fg='red',bg='#1A1A1C')
                creer_utilisateur.config(font= ('verdana' ,8 ,'normal' ))
                creer_utilisateur.place(x=5,y=3)
                creer_entry_utilisateur = Entry(creationuser)
                creer_entry_utilisateur.place(x=140,y=5)
                #Mot de passe
                creer_mot_de_passe = Label(creationuser, text='Mot de passe :',fg='red',bg='#1A1A1C')
                creer_mot_de_passe.config(font= ('verdana' ,8,'normal'))
                creer_mot_de_passe.place(x=5,y=50)
                creer_entry_mot_de_passe = Entry(creationuser)
                creer_entry_mot_de_passe.place(x=140,y=52)
                conf_mot_de_passe = Label(creationuser, text='Confirmer :',fg='red',bg='#1A1A1C')
                conf_mot_de_passe.config(font= ('verdana' ,8,'normal'))
                conf_mot_de_passe.place(x=5,y=83)
                conf_entry_mot_de_passe = Entry(creationuser)
                conf_entry_mot_de_passe.place(x=140,y=85)
                creer_le_compte = Button(creationuser, text='CréerLecompte', command=creer_le_compte)
                creer_le_compte.config(bg='black',fg="white")
                creer_le_compte.place(x=200,y=120)
                log_out=Button(creationuser, text="Retour", command=creationuser.destroy)
                log_out.config(bg='red',fg="white")
                log_out.place(x=5,y=120)
                login.mainloop()
            #Bouton Connection et Création de compte
            Connection = Button(login, text='Connection',command=connexionuser)
            Connection.config(bg='black',fg="white")
            Connection.place(x=50,y=180)
            creer_compte = Button(login, text='Creer un compte',command=creation_account)
            creer_compte.config(bg='red',fg="white")
            creer_compte.place(x=150,y=180)
            login.mainloop()
 
def Panier():
            #Fenetre du panier
            global Divison,final,ghost,switch,ps5,nba2k,manette,paniertotal
            prix_manette=0
            prix_ps5=0
            prix_divison=0
            prix_switch=0
            prix_ff7=0
            prix_nba=0
            prix_ghost=0
 
 
            Panier = Toplevel()
            Panier.title("Panier")
            w=350 
            h=285 
            ws=Panier.winfo_screenwidth() 
            hs=Panier.winfo_screenheight() 
            x=(ws/2.05)-(w/1.2) 
            y=(hs/3.9)-(h/2)
            Panier.geometry('+%d+%d'%(x,y)) 
            Panier.config(width=425,height=500,bg='#1A1A1C')
            
            #Fenetre en mode pop-up
            if connecter is False:
                error = Label(Panier, text='Veuillez vous identifier',fg='red',bg='#1A1A1C')
                error.config(font= ('verdana' ,12 ,'normal'))
                error.place(x=120,y=200)
 
            else:
                if final is None and ghost is None and Divison is None and switch is None and ps5 is None and nba2k is None and manette is None and paniertotal is None:
                    panier_vide = Label(Panier, text='Votre panier est vide',fg='red',bg='#1A1A1C')
                    panier_vide.config(font= ('verdana' ,12 ,'normal'))
                    panier_vide.place(x=120,y=200)
                else:
 
                    #Affichage de vente de FF7 dans le panier
                    if final is not None:
                        prix_ff7 = float(final)*38.97
                        txt_final = Label(Panier, text='final : X'+str(final)+', Prix : '+str(format(prix_ff7,'.2f'))+' €',fg='#989C40',bg='#1A1A1C')
                        txt_final.config(font= ('verdana' ,12 ,'normal' ))
                        txt_final.place(x=5,y=15)
                        btn_plus_final=Button(Panier, text='+',bg='#1A1A1C',fg='red',bd=0,command=plusfinal)
                        btn_plus_final.config(font= ('verdana' ,12 ,'normal' ))
                        btn_plus_final.place(x=300, y=15)
                        btn_moins_final=Button(Panier, text='-',bg='#1A1A1C',fg='red',bd=0,command=moinsfinal)
                        btn_moins_final.config(font= ('verdana' ,12 ,'normal' ))
                        btn_moins_final.place(x=340, y=15)
                    #Affichage de vente de The divison  dans le panier
                    if Divison is not None:
                        prix_divison = float(Divison)*45.95
                        txt_div = Label(Panier, text='The divison: X'+str(Divison)+', Prix : '+str(format(prix_divison,'.2f'))+' €',fg='#989C40',bg='#1A1A1C')
                        txt_div.config(font= ('verdana' ,12 ,'normal' ))
                        txt_div.place(x=5,y=45)
                        btn_plus_div=Button(Panier, text='+',bg='#1A1A1C',fg='red',bd=0,command=plusdivision)
                        btn_plus_div.config(font= ('verdana' ,12 ,'normal' ))
                        btn_plus_div.place(x=300, y=45)
                        btn_moins_div=Button(Panier, text='-',bg='#1A1A1C',fg='red',bd=0,command=moinsdivsion)
                        btn_moins_div.config(font= ('verdana' ,12 ,'normal' ))
                        btn_moins_div.place(x=340, y=45)
                    #Affichage de vente de Nintendo Switch dans le panier
                    if switch is not None:
                        prix_switch = float(switch)*310.99
                        txt_switch = Label(Panier, text='Nintendo Switch: X'+str(switch)+', Prix : '+str(format(prix_switch,'.2f'))+' €',fg='#989C40',bg='#1A1A1C')
                        txt_switch.config(font= ('verdana' ,12 ,'normal' ))
                        txt_switch.place(x=5,y=75)
                        btn_plus_switch=Button(Panier, text='+',bg='#1A1A1C',fg='red',bd=0,command=plus_switch)
                        btn_plus_switch.config(font= ('verdana' ,12 ,'normal' ))
                        btn_plus_switch.place(x=300, y=75)
                        btn_moins_switch=Button(Panier, text='-',bg='#1A1A1C',fg='red',bd=0,command=moins_switch)
                        btn_moins_switch.config(font= ('verdana' ,12 ,'normal' ))
                        btn_moins_switch.place(x=340, y=75)
                    #Affichage de vente de Ps5 dans le panier
                    if ps5 is not None:
                        prix_ps5 = float(ps5)*499.99
                        txt_ps5 = Label(Panier, text='ps5: X'+str(ps5)+', Prix : '+str(prix_ps5)+' €',fg='#989C40',bg='#1A1A1C')
                        txt_ps5.config(font= ('verdana' ,12 ,'normal' ))
                        txt_ps5.place(x=5,y=105)
                        btn_plus_ps5=Button(Panier, text='+',bg='#1A1A1C',fg='red',bd=0,command=plusps5)
                        btn_plus_ps5.config(font= ('verdana' ,12 ,'normal' ))
                        btn_plus_ps5.place(x=300, y=105)
                        btn_moins_ps5=Button(Panier, text='-',bg='#1A1A1C',fg='red',bd=0,command=moinsps5)
                        btn_moins_ps5.config(font= ('verdana' ,12 ,'normal' ))
                        btn_moins_ps5.place(x=340, y=105)
                    #Affichage de vente de Nba2k dans le panier
                    if nba2k is not None:
                        prix_nba = float(nba2k)*69.95
                        txt_nba = Label(Panier, text='nba2k: X'+str(nba2k)+', Prix : '+str(format(prix_nba,'.2f'))+' €',fg='#989C40',bg='#1A1A1C')
                        txt_nba.config(font= ('verdana' ,12 ,'normal' ))
                        txt_nba.place(x=5,y=135)
                        paniertotal=str(prix_manette+prix_ghost+prix_nba+prix_ps5+prix_switch+prix_divison+prix_ff7)
                        btn_plus_nba=Button(Panier, text='+',bg='#1A1A1C',fg='red',bd=0,command=plusnba)
                        btn_plus_nba.config(font= ('verdana' ,12 ,'normal' ))
                        btn_plus_nba.place(x=300, y=135)
                        btn_moins_nba=Button(Panier, text='-',bg='#1A1A1C',fg='red',bd=0,command=Moinsnba)
                        btn_moins_nba.config(font= ('verdana' ,12 ,'normal' ))
                        btn_moins_nba.place(x=340, y=135)
 
                    #Affichage de vente de Ghost dans le panier
                    if ghost is not None:
                        prix_ghost = float(ghost)*20.95
                        txt_ghost = Label(Panier, text='ghost: X'+str(ghost)+', Prix : '+str(format(prix_ghost,'.2f'))+' €',fg='#989C40',bg='#1A1A1C')
                        txt_ghost.config(font= ('verdana' ,12 ,'normal' ))
                        txt_ghost.place(x=5,y=165)
                        btn_plus_ghost=Button(Panier, text='+',bg='#1A1A1C',fg='red',bd=0,command=plusghost)
                        btn_plus_ghost.config(font= ('verdana' ,12 ,'normal' ))
                        btn_plus_ghost.place(x=300, y=165)
                        btn_moins_ghost=Button(Panier, text='-',bg='#1A1A1C',fg='red',bd=0,command=moinsghost)
                        btn_moins_ghost.config(font= ('verdana' ,12 ,'normal' ))
                        btn_moins_ghost.place(x=340, y=165)
                    #Affichage de vente de Manette dans le panier
                    if manette is not None:
                        prix_manette = float(manette)*49.99
                        txt_manette = Label(Panier, text='Manette : X'+str(manette)+', Prix : '+str(format(prix_manette,'.2f'))+' €',fg='#989C40',bg='#1A1A1C')
                        txt_manette.config(font= ('verdana' ,12 ,'normal' ))
                        txt_manette.place(x=5,y=195)
                        btn_plus_manette=Button(Panier, text='+',bg='#1A1A1C',fg='red',bd=0,command=plusmanette)
                        btn_plus_manette.config(font= ('verdana' ,12 ,'normal' ))
                        btn_plus_manette.place(x=300, y=195)
                        btn_moins_manette=Button(Panier, text='-',bg='#1A1A1C',fg='red',bd=0,command=moinsmanette)
                        btn_moins_manette.config(font= ('verdana' ,12 ,'normal' ))
                        btn_moins_manette.place(x=340, y=195)
                    #Affichage prix total du panier
                    if final is not None or ghost is not None or Divison is not None or switch is not None or ps5 is not None or nba2k is not None or manette is not None or paniertotal is not None:
                        paniertotal=str(prix_manette+prix_ghost+prix_nba+prix_ps5+prix_switch+prix_divison+prix_ff7)
                        txt_panier_total=Label(Panier, text='Prix total : '+str(paniertotal)+' €',fg='antiquewhite',bg='#1A1A1C')
                        txt_panier_total.config(font= ('verdana' ,16 ,'normal' ))
                        txt_panier_total.place(x=65,y=320)
 
                
 
 
#ajouter au panier dans la fenetre principal FF7
def ajouter_final():
    global texte
    global final
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    if connecter is True:
        final = int(entry_final.get())
        entree_ff7 = int(entry_final.get())
        entree_ff7 = entree_ff7 + 1
        entry_final.delete(0,END)
        entry_final.insert(0,entree_ff7)
bouton_final = Button(fenetre, image=panier, command=ajouter_final,bg='#1A1A1C',bd=0)
bouton_final.place(x=500, y=510)
 
entry_final = Entry()
entry_final.place(x=500, y=545)
entry_final.config(width=3)
entry_final.insert(0,'1')
#ajouter dans le panier l'article
def plusfinal():
        entree_ff7 = int(entry_final.get())
        entree_ff7 = entree_ff7 + 1
        entry_final.delete(0,END)
        entry_final.insert(0,entree_ff7)
#enlever un article dans le panier
def moinsfinal():
    entree_ff7 = int(entry_final.get())
    if entree_ff7 > 0:
        entree_ff7 = entree_ff7 - 1
        entry_final.delete(0,END)
        entry_final.insert(0,entree_ff7)
 
#ajouter au panier dans la fenetre principal nba2k
def ajouter_nba():
    global texte
    global nba2k
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    if connecter is True:
        nba2k = int(entry_nba22.get())
        entree_nba = int(entry_nba22.get())
        entree_nba = entree_nba + 1
        entry_nba22.delete(0,END)
        entry_nba22.insert(0,entree_nba)
bouton_nba = Button(fenetre, image=panier, command=ajouter_nba,bg='#1A1A1C',bd=0)
bouton_nba.place(x=800, y=510)
 
entry_nba22 = Entry()
entry_nba22.place(x=800, y=545)
entry_nba22.config(width=3)
entry_nba22.insert(0,'1') 
#ajouter dans le panier l'article   
def plusnba():
        entree_nba = int(entry_nba22.get())
        entree_nba = entree_nba + 1
        entry_nba22.delete(0,END)
        entry_nba22.insert(0,entree_nba)
#enlever un article dans le panier
def Moinsnba():
    entree_nba = int(entry_nba22.get())
    if entree_nba > 0:
        entree_nba = entree_nba - 1
        entry_nba22.delete(0,END)
        entry_nba22.insert(0,entree_nba)
 
 
 
entry_nba22 = Entry()
entry_nba22.place(x=800, y=545)
entry_nba22.config(width=3)
entry_nba22.insert(0,'1')
 
#ajouter au panier dans la fenetre principal The divison
def ajouter_div():
    global texte
    global Divison
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    if connecter is True:
        Divison = int(entry_Division.get())
        entree_div = int(entry_Division.get())
        entree_div = entree_div + 1
        entry_Division.delete(0,END)
        entry_Division.insert(0,entree_div)
bouton_div = Button(fenetre, image=panier, command=ajouter_div,bg='#1A1A1C',bd=0)
bouton_div.place(x=195, y=510)
 
entry_Division = Entry()
entry_Division.place(x=195, y=545)
entry_Division.config(width=3)
entry_Division.insert(0,'1')
#ajouter dans le panier l'article
def plusdivision():
        entree_div = int(entry_Division.get())
        entree_div = entree_div + 1
        entry_Division.delete(0,END)
        entry_Division.insert(0,entree_div)
#enlever un article dans le panier
def moinsdivsion():
    entree_div = int(entry_Division.get())
    if entree_div > 0:
        entree_div = entree_div - 1
        entry_Division.delete(0,END)
        entry_Division.insert(0,entree_div)
 
 
#ajouter au panier dans la fenetre principal Nintendo Switch
def ajouter_nintswitch():
    global texte
    global switch
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    if connecter is True:
        switch = int(entry_SWITCH.get())
        entree_switch = int(entry_SWITCH.get())
        entree_switch = entree_switch + 1
        entry_SWITCH.delete(0,END)
        entry_SWITCH.insert(0,entree_switch)
bouton_switch = Button(fenetre, image=panier, command=ajouter_nintswitch,bg='#1A1A1C',bd=0)
bouton_switch.place(x=1030, y=880)
 
 
entry_SWITCH = Entry()
entry_SWITCH.place(x=1030, y=915)
entry_SWITCH.config(width=3)
entry_SWITCH.insert(0,'1')
#ajouter dans le panier l'article
def plus_switch():
        entree_switch = int(entry_SWITCH.get())
        entree_switch = entree_switch + 1
        entry_SWITCH.delete(0,END)
        entry_SWITCH.insert(0,entree_switch)
#enlever un article dans le panier
def moins_switch():
    entree_switch = int(entry_SWITCH.get())
    if entree_switch > 0:
        entree_switch = entree_switch - 1
        entry_SWITCH.delete(0,END)
        entry_SWITCH.insert(0,entree_switch)
 
#ajouter au panier dans la fenetre principal ps5
def ajouter_ps5():
    global texte
    global ps5
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    if connecter is True:
        ps5 = int(entry_ps5.get())
        entree_ps5 = int(entry_ps5.get())
        entree_ps5 = entree_ps5 + 1
        entry_ps5.delete(0,END)
        entry_ps5.insert(0,entree_ps5)
bouton_ps5 = Button(fenetre, image=panier, command=ajouter_ps5,bg='#1A1A1C',bd=0)
bouton_ps5.place(x=695, y=880)
 
 
entry_ps5 = Entry()
entry_ps5.place(x=695, y=915)
entry_ps5.config(width=3)
entry_ps5.insert(0,'1')
#ajouter dans le panier l'article
def plusps5():
        entree_ps5 = int(entry_ps5.get())
        entree_ps5 = entree_ps5 + 1
        entry_ps5.delete(0,END)
        entry_ps5.insert(0,entree_ps5)
 
#enlever un article dans le panier
def moinsps5():
    entree_ps5 = int(entry_ps5.get())
    if entree_ps5 > 0:
        entree_ps5 = entree_ps5 - 1
        entry_ps5.delete(0,END)
        entry_ps5.insert(0,entree_ps5)
 
 
#ajouter au panier dans la fenetre principal Ghost
def ajouter_ghost():
    global texte
    global ghost
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    if connecter is True:
        ghost = int(entry_ghost.get())
        entree_ghost = int(entry_ghost.get())
        entree_ghost = entree_ghost + 1
        entry_ghost.delete(0,END)
        entry_ghost.insert(0,entree_ghost)
bouton_ghost = Button(fenetre, image=panier, command=ajouter_ghost,bg='#1A1A1C',bd=0)
bouton_ghost.place(x=1097, y=510)
 
entry_ghost = Entry()
entry_ghost.place(x=1097, y=545)
entry_ghost.config(width=3)
entry_ghost.insert(0,'1')
#ajouter dans le panier l'article
def plusghost():
        entree_ghost = int(entry_ghost.get())
        entree_ghost = entree_ghost + 1
        entry_ghost.delete(0,END)
        entry_ghost.insert(0,entree_ghost)
#enlever un article dans le panier
def moinsghost():
    entree_ghost = int(entry_ghost.get())
    if entree_ghost > 0:
        entree_ghost = entree_ghost - 1
        entry_ghost.delete(0,END)
        entry_ghost.insert(0,entree_ghost)
 
 
 
#ajouter au panier dans la fenetre principal Manette
def ajouter_manette():
    global texte
    global manette
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    if connecter is True:
        manette = int(entry_manette.get())
        entree_manete = int(entry_manette.get())
        entree_manete = entree_manete + 1
        entry_manette.delete(0,END)
        entry_manette.insert(0,entree_manete)
bouton_manette = Button(fenetre, image=panier, command=ajouter_manette,bg='#1A1A1C',bd=0)
bouton_manette.place(x=230, y=880)
entry_manette = Entry()
entry_manette.place(x=230, y=915)
entry_manette.config(width=3)
entry_manette.insert(0,'1')
#ajouter dans le panier l'article
def plusmanette():
        entree_manete = int(entry_manette.get())
        entree_manete = entree_manete + 1
        entry_manette.delete(0,END)
        entry_manette.insert(0,entree_manete)
 
#enlever un article dans le panier
def moinsmanette():
    entree_manete = int(entry_manette.get())
    if entree_manete > 0:
        entree_manete = entree_manete - 1
        entry_manette.delete(0,END)
        entry_manette.insert(0,entree_manete)
 
#descriptif de Final Fantaisy VII
def presentation_ff7():
    detail = Toplevel()
    detail.title("Detail/FinalFantasyVII.dz")
    w=350 
    h=285 
    ws=detail.winfo_screenwidth() 
    hs=detail.winfo_screenheight() 
    x=(ws/2.9)-(w/1.2) 
    y=(hs/2.5)-(h/2)
    detail.geometry('+%d+%d'%(x,y)) 
    detail.config(width=400,height=250,bg='#1A1A1C')
    detail_div_titre = Label(detail, text="Final Fantasy VII",fg='#951717',bg='#1A1A1C')
    detail_div_titre.config(font= ('verdana' ,18 ,'normal' ))
    detail_div_titre.place(x=100,y=10)   
    detail_div = Label(detail, text="Final Fantasy VII est un jeu vidéo\n  de rôle développé par Square sous \n la direction de Yoshinori Kitase et sorti en 1997, \n constituant le septième opus de la série Final Fantasy,\n  ces un jeux qui ce joue en solo\n\n 38.97€",fg='#E4E5DD',bg='#1A1A1C')
    detail_div.config(font= ('verdana' ,10 ,'normal' ))
    detail_div.place(x=10,y=100) 
 
bouton_present_div=Button(fenetre, image=FF7,command=presentation_ff7,bd=0,bg='#1A1A1C')
bouton_present_div.place(x=448,y=255)
 
#descriptif de Final Fantaisy VII
def presentation_divison():
    detail = Toplevel()
    detail.title("Detail/Thedivison2.dz")
    w=350 
    h=285 
    ws=detail.winfo_screenwidth() 
    hs=detail.winfo_screenheight() 
    x=(ws/4.6)-(w/1.2) 
    y=(hs/2.5)-(h/2)
    detail.geometry('+%d+%d'%(x,y)) 
    detail.config(width=450,height=250,bg='#1A1A1C')
    detail_final_titre = Label(detail, text="The divison 2",fg='#951717',bg='#1A1A1C')
    detail_final_titre.config(font= ('verdana' ,18 ,'normal' ))
    detail_final_titre.place(x=150,y=10)   
    detail_final = Label(detail, text="Tom Clancy's The Division 2 est\n   un RPG de tir avec des modes campagne,\n   coopération et PvP qui offre plus de variété de\n   missions et de défis, de nouveaux systèmes de progression\n   avec des rebondissements et des surprises\n   uniques et de nouvelles innovations qui offrent\n   de nouvelles façons de jouer.\n\n 45.95€",fg='#E4E5DD',bg='#1A1A1C')
    detail_final.config(font= ('verdana' ,10 ,'normal' ))
    detail_final.place(x=0,y=100)
bouton_present_div=Button(fenetre, image=DIVSION,command=presentation_divison,bd=0,bg='#1A1A1C')
bouton_present_div.place(x=150,y=243)
 
#descriptif de Final Fantaisy VII
def presentation_nba():
    detail = Toplevel()
    detail.title("Detail/Nba2k.fr")
    w=350 
    h=285 
    ws=detail.winfo_screenwidth() 
    hs=detail.winfo_screenheight() 
    x=(ws/1.8)-(w/1.2) 
    y=(hs/2.5)-(h/2)
    detail.geometry('+%d+%d'%(x,y)) 
    detail.config(width=450,height=250,bg='#1A1A1C')
    detail_final_titre = Label(detail, text="Nba2k",fg='#951717',bg='#1A1A1C')
    detail_final_titre.config(font= ('verdana' ,18 ,'normal' ))
    detail_final_titre.place(x=200,y=10)   
    detail_final = Label(detail, text="Solo, multijoueur.\n  NBA 2K20 est un jeu vidéo de simulation de basket développé par\n  Visual Concepts et publié par 2K Sports, \n basé sur la National  Basketball Association (NBA).\n  C'est le 21e épisode de la franchise NBA 2K, \n le successeur de NBA 2K19 et le prédécesseur de NBA 2K21\n\n 69.95€",fg='#E4E5DD',bg='#1A1A1C')
    detail_final.config(font= ('verdana' ,10 ,'normal' ))
    detail_final.place(x=0,y=100)
bouton_present_div=Button(fenetre, image=NBA,command=presentation_nba,bd=0,bg='#1A1A1C')
bouton_present_div.place(x=750,y=255)
#descriptif de Final Fantaisy VII
def presentation_ps5():
    detail = Toplevel()
    detail.title("Detail/ps5.dz")
    w=350 
    h=285 
    ws=detail.winfo_screenwidth() 
    hs=detail.winfo_screenheight() 
    x=(ws/2.2)-(w/1.2) 
    y=(hs/1.2)-(h/2.5)
    detail.geometry('+%d+%d'%(x,y)) 
    detail.config(width=555,height=220,bg='#1A1A1C')
    detail_final_titre = Label(detail, text="Playstation 5",fg='#951717',bg='#1A1A1C')
    detail_final_titre.config(font= ('verdana' ,18 ,'normal' ))
    detail_final_titre.place(x=200,y=10)   
    detail_final = Label(detail, text="la PS5 (et son alternative numérique) bascule un processeur\n  AMD Zen 2 avec 8 cœurs à 3,5 GHz\n ,16 Go de mémoire GDDR6 et un GPU RDNA 2 AMD personnalisé cela produit 10,28\n  TFLOP de puissance de traitement.\n\n 499.99€",fg='#E4E5DD',bg='#1A1A1C')
    detail_final.config(font= ('verdana' ,10 ,'normal' ))
    detail_final.place(x=0,y=100)
bouton_present_div=Button(fenetre, image=PS5,command=presentation_ps5,bd=0,bg='#1A1A1C')
bouton_present_div.place(x=560,y=700)
 
#descriptif de Nintendo Switch
def presentation_switch():
    detail = Toplevel()
    detail.title("Detail/Nba2k.dz")
    w=350 
    h=285 
    ws=detail.winfo_screenwidth() 
    hs=detail.winfo_screenheight() 
    x=(ws/1.4)-(w/1.4) 
    y=(hs/1.2)-(h/2.5)
    detail.geometry('+%d+%d'%(x,y)) 
    detail.config(width=600,height=200,bg='#1A1A1C')
    detail_final_titre = Label(detail, text="Nintendo Switch",fg='#951717',bg='#1A1A1C')
    detail_final_titre.config(font= ('verdana' ,18 ,'normal' ))
    detail_final_titre.place(x=200,y=10)   
    detail_final = Label(detail, text="La Nintendo Switch est une console de jeu vidéo hybride,\n composée d'une console, d'une station d'accueil et de deux contrôleurs Joy-Con.\n Bien qu'il s'agisse d'une console hybride,\n Nintendo la classe comme \n«une console de salon que vous pouvez emporter avec vous lors de vos déplacements».\n\n 310.99€",fg='#E4E5DD',bg='#1A1A1C')
    detail_final.config(font= ('verdana' ,10 ,'normal' ))
    detail_final.place(x=0,y=80)
bouton_present_div=Button(fenetre, image=SWITCHE,command=presentation_switch,bd=0,bg='#1A1A1C')
bouton_present_div.place(x=950,y=685)
#descriptif de Ghost
def presentation_ghost():
    detail = Toplevel()
    detail.title("Detail/Ghost.dz")
    w=350 
    h=285 
    ws=detail.winfo_screenwidth() 
    hs=detail.winfo_screenheight() 
    x=(ws/1.4)-(w/1.4) 
    y=(hs/2)-(h/2)
    detail.geometry('+%d+%d'%(x,y)) 
    detail.config(width=450,height=230,bg='#1A1A1C')
    detail_final_titre = Label(detail, text="Ghost",fg='#951717',bg='#1A1A1C')
    detail_final_titre.config(font= ('verdana' ,18 ,'normal' ))
    detail_final_titre.place(x=170,y=10)   
    detail_final = Label(detail, text="C'est un jeu d'action dans lequel le joueur incarne un samouraï \n (Jin Sakai) en quête de vengeance contre les envahisseurs\n mongols dans le Japon du 13e siècle. ... \nLes joueurs utilisent des épées de samouraïs,\n des fléchettes empoisonnées et des arcs pour affronter\n des ennemis dans des combats de style mêlée\n\n 20.95€",fg='#E4E5DD',bg='#1A1A1C')
    detail_final.config(font= ('verdana' ,10 ,'normal' ))
    detail_final.place(x=0,y=80)
bouton_present_div=Button(fenetre, image=GHOST,command=presentation_ghost,bd=0,bg='#1A1A1C')
bouton_present_div.place(x=1045,y=255)
#descriptif de Manette
def presentation_manette():
    detail = Toplevel()
    detail.title("Detail/Manette.dz")
    w=350 
    h=285 
    ws=detail.winfo_screenwidth() 
    hs=detail.winfo_screenheight() 
    x=(ws/3.6)-(w/1.2) 
    y=(hs/1.2)-(h/2.5)
    detail.geometry('+%d+%d'%(x,y)) 
    detail.config(width=450,height=150,bg='#1A1A1C')
    detail_final_titre = Label(detail, text="Manette Ps4",fg='#951717',bg='#1A1A1C')
    detail_final_titre.config(font= ('verdana' ,18 ,'normal' ))
    detail_final_titre.place(x=140,y=10)   
    detail_final = Label(detail, text="Manette pour Ps4 utilisable sur la Ps4 est\n aussi sur Ordinateur avec adaptateur.\n\n 49.99€",fg='#E4E5DD',bg='#1A1A1C')
    detail_final.config(font= ('verdana' ,10 ,'normal' ))
    detail_final.place(x=80,y=80)
bouton_present_div=Button(fenetre, image=MANETTE,command=presentation_manette,bd=0,bg='#1A1A1C')
bouton_present_div.place(x=125,y=685)
 
panieeee=Button(image=paniere,command=Panier,bd=0,bg='#1A1A1C')
panieeee.place(x=650,y=10)
 
fenetre.bind('<Button-1>', cliquegauche)
fenetre.mainloop()
 

