## Mettre le terminal grand ouvert - Important afin de voir l'ensemble des informations données par le programme

import random

# Fonction pour calculer le prix de revente aléatoire en pourcentage positif ou négatif
def prix_revente(prix_initial):
    variation = random.randint(-30, 30)  # Variation aléatoire entre 20% et 30%
    prix_revente = prix_initial + (prix_initial * (variation // 100))
    return prix_revente

evenement = random.randint(1,15) #Evenement aléatoire pour la fluctuation du marché

#Fonction pour l'affichage de l'evenement aléatoire
def affichage():
    if evenement == 1 :
       print("\nUne guerre a eclaté en Russie ! Attention, le marché sera impacté.")
    if evenement == 2 :
        print("\nVous êtes affecté par une crise économique ! Attention, le marché sera impacté.")
    if evenement == 3 :
        print("\nUn scandale financier majeur dans une grande entreprise a été découvert. Attention, le marché sera impacté.")
    if evenement == 4 :
        print("\nUn tremblement de terre a eu lieu au Maroc. Attention, le marché sera impacté.")
    if evenement == 5 :
        print("\nLa société Générale a fait faillite ! Attention, le marché sera impacté.")
    if evenement == 6 :
        print("\nLes JO de 2024 approchent à grands pas. Attention, le marché sera impacté.")
    if evenement == 7 :
        print("\nUne pandémie vient d'apparaître ! Attention, le marché sera impacté.")
    if evenement == 8 :
        print("\nUne baisse significative des taux d'inflation a été perçue ! Attention, le marché sera impacté.")


#Fonction du prix de revente d'une action
def prix_revente2(prix_initial):
    if evenement == 1 :
        prix_revente3 = prix_revente(prix_initial) // 2
    if evenement == 2 :
        prix_revente3 = prix_revente(prix_initial) // 2
    if evenement == 3 :
        prix_revente3 = prix_revente(prix_initial) // 2
    if evenement == 4 :
        prix_revente3 = prix_revente(prix_initial) // 2
    if evenement == 5 :
        prix_revente3 = prix_revente(prix_initial) // 2
    if evenement == 6 :
        prix_revente3 = prix_revente(prix_initial) * 2
    if evenement == 7 :
        prix_revente3 = prix_revente(prix_initial) // 4
    if evenement == 8 :
        prix_revente3 = prix_revente(prix_initial) * 3
    else :
        prix_revente3 = prix_revente(prix_initial)
    return prix_revente3

#Fonction pour le prix d'achat d'une action
def prix_1(prix_initial):
    if evenement == 1 :
        return prix_initial // 2
    if evenement == 2 :
        return prix_initial // 4
    if evenement == 3 :
        return prix_initial // 3
    if evenement == 4 :
        return prix_initial // 2
    if evenement == 5 :
        return prix_initial // 3
    if evenement == 6 :
        return prix_initial * 2
    if evenement == 7 :
        return prix_initial // 4
    if evenement == 8 :
        return prix_initial * 4
    else :
        return prix_initial


# Initialisation des variables

nom_joueur = input("Bonjour ! Quel est votre nom ? ")
argent = 1000  # Le joueur commence avec 1 000 euros
objectif_argent = 10000  # L'objectif est d'atteindre 10 000 euros
actions = 0 #Le nombre d'actions possédées par le joueur
prix_action = 0 


#Fonction d'achat d'actions
def achat_actions():
        afficher_infos_joueur()
        global argent, actions, prix_action
        entreprise_choisie = input("\nChoisissez une entreprise : ")
        if entreprise_choisie == "LVMH" or entreprise_choisie == "Airbus" or entreprise_choisie == "Apple" or entreprise_choisie == "Amazon" or entreprise_choisie == "Sanofi" or entreprise_choisie == "Safran" or entreprise_choisie == "Orange" or entreprise_choisie == "Bouygues" or entreprise_choisie == "Dassault" or entreprise_choisie == "Engie":
            print("\nCombien d'actions de ", end="")
            print(entreprise_choisie, end="")
            montant_achat = int(input(" voulez-vous acheter ?")) 
            if montant_achat <= 0:
                print("Montant d'actions non valide.")
                achat_actions()
            if montant_achat > argent :
                print("Vous n'avez pas assez d'argent pour acheter autant d'actions.")
                achat_actions()
            if entreprise_choisie == "LVMH" :
                prix_action = prix_lvmh
            if entreprise_choisie == "Airbus" :
                prix_action = prix_airbus
            if entreprise_choisie == "Apple" :
                prix_action = prix_apple
            if entreprise_choisie == "Amazon" :
                prix_action = prix_amazon
            if entreprise_choisie == "Sanofi" :
                prix_action = prix_sanofi
            if entreprise_choisie == "Safran" :
                prix_action = prix_safran
            if entreprise_choisie == "Orange" :
                prix_action = prix_orange
            if entreprise_choisie == "Bouygues" :
                prix_action = prix_bouygues
            if entreprise_choisie == "Dassault" :
                prix_action = prix_dassault
            if entreprise_choisie == "Engie" :
                prix_action = prix_engie
            else :
                argent = argent - (montant_achat*prix_action)
                actions = actions + montant_achat
            afficher_infos_joueur()
        else :
            print("Vous n'avez pas correctement écrit le nom d'une entreprise")


#Fonction de vente d'actions
def vente_actions():       
    afficher_infos_joueur()
    global argent, actions
    entreprise_choisie = input("\nChoisissez une action à vendre : ")
    if entreprise_choisie == "LVMH" or entreprise_choisie == "Airbus" or entreprise_choisie == "Apple" or entreprise_choisie == "Amazon" or entreprise_choisie == "Sanofi" or entreprise_choisie == "Safran" or entreprise_choisie == "Orange" or entreprise_choisie == "Bouygues" or entreprise_choisie == "Dassault" or entreprise_choisie == "Engie":
        print("\nCombien d'actions de ", end="")
        print(entreprise_choisie, end="")
        montant_vente = int(input(" Voulez-vous vendre ?"))
        if entreprise_choisie == "LVMH" :
            prix_action = prix_revente_lvmh
        if entreprise_choisie == "Airbus" :
            prix_action = prix_revente_airbus
        if entreprise_choisie == "Apple" :
            prix_action = prix_revente_apple
        if entreprise_choisie == "Amazon" :
            prix_action = prix_revente_amazon
        if entreprise_choisie == "Sanofi" :
            prix_action = prix_revente_sanofi
        if entreprise_choisie == "Safran" :
            prix_action = prix_revente_safran
        if entreprise_choisie == "Orange" :
            prix_action = prix_revente_orange
        if entreprise_choisie == "Bouygues" :
            prix_action = prix_revente_bouygues
        if entreprise_choisie == "Dassault" :
            prix_action = prix_revente_dassault
        if entreprise_choisie == "Engie" :
            prix_action = prix_revente_engie
        if montant_vente <= 0 :
            print("Montant d'actions invalide.")
        else :
            argent = argent + (prix_action * montant_vente)
            actions = actions - montant_vente
            afficher_infos_joueur()
    else :
        print("Vous n'avez pas écrit correctement le nom d'une entreprise")
        vente_actions()

#Fonction qui affiche les infos du joueur
def afficher_infos_joueur():
    print("\nBonjour", nom_joueur, "vous avez", argent, "euros et", actions, "actions au total.") ##Mettre une estimation de valeur des actions au total et quels actions le joueur a



#Intéractions avec le joueur et début du jeu
print("\nBonjour", nom_joueur, "! Bienvenue dans le jeu d'achat et de vente d'actions. \nVous devez acheter et vendre des actions afin de gagner de l'argent. \nCependant, faites attention à la fluctuation du marché qui pourra rendre vos efforts inutiles.")
print("Vous commencez avec 1 000 euros. Votre objectif est d'atteindre 10 000 euros. Bonne chance. ")
choix=input("\nAcceptez-vous le défi ? (oui/non) ")
if choix == "non":
    print("Dommage, vous auriez pu gagner 10 000 euros !")
else:
    while argent < objectif_argent :

       
       #Initaialisation des prix d'actions à l'achat à chaque ittération
        prix_lvmh = prix_1(200)
        prix_airbus = prix_1(100)
        prix_apple = prix_1(150)
        prix_amazon = prix_1(300)
        prix_sanofi = prix_1(50)
        prix_safran = prix_1(75)
        prix_orange = prix_1(25)
        prix_bouygues = prix_1(55)
        prix_dassault = prix_1(70)
        prix_engie = prix_1(80)

        #Initaialisation des prix d'actions à la revente à chaque ittération
        prix_revente_lvmh = prix_revente2(200)
        prix_revente_airbus = prix_revente2(100)
        prix_revente_apple = prix_revente2(150)
        prix_revente_amazon = prix_revente2(300)
        prix_revente_sanofi = prix_revente2(50)
        prix_revente_safran = prix_revente2(75)
        prix_revente_orange = prix_revente2(25)
        prix_revente_bouygues = prix_revente2(55)
        prix_revente_dassault = prix_revente2(70)
        prix_revente_engie = prix_revente2(80)

       
       #Affichage des différentes fluctuations du marché et nouvel valeur pour evenement à chaque ittération
        
        evenement = random.randint(1,5)
        affichage()
        
        #Affichage des différentes actions disponibles
        print("\nVoici les actions disponibles à l'achat:")
        print("\nLVMH: Prix de l'action - ", prix_lvmh, " euros, " "Prix de revente estimé - ", prix_revente_lvmh, "euros")
        print("\nAirbus: Prix de l'action - ", prix_airbus, " euros, " "Prix de revente estimé - ", prix_revente_airbus, "euros")
        print("\nApple: Prix de l'action - ", prix_apple, " euros, " "Prix de revente estimé - ", prix_revente_apple, "euros")
        print("\nAmazon: Prix de l'action - ", prix_amazon, " euros, " "Prix de revente estimé - ", prix_revente_amazon, "euros")
        print("\nSanofi: Prix de l'action - ", prix_sanofi, " euros, " "Prix de revente estimé - ", prix_revente_sanofi, "euros")
        print("\nSafran: Prix de l'action - ", prix_safran, " euros, " "Prix de revente estimé - ", prix_revente_safran, "euros")
        print("\nOrange: Prix de l'action - ", prix_orange, " euros, " "Prix de revente estimé - ", prix_revente_orange, "euros")
        print("\nBouygues: Prix de l'action - ", prix_bouygues, " euros, " "Prix de revente estimé - ", prix_revente_bouygues, "euros")
        print("\nDassault: Prix de l'action - ", prix_dassault, " euros, " "Prix de revente estimé - ", prix_revente_dassault, "euros")
        print("\nEngie: Prix de l'action - ", prix_engie, " euros, " "Prix de revente estimé - ", prix_revente_engie, "euros")

        reponse = input("\nVoulez-vous acheter, vendre des actions ou ne rien faire ? (acheter/vendre/non) ")

        if reponse == "acheter" or reponse == "vendre" or reponse == "non":
            if reponse == "acheter" :
                achat_actions()
            if reponse == "vendre" :
                vente_actions()
            if reponse == "non" :
                reponse
        else :
            print("\nVous n'avez pas correctement écrit (acheter/vendre).\nRetentez votre chance.")
            reponse

if argent >= objectif_argent:
    print("\nBravo ! ", nom_joueur, "Vous avez atteint 10 000 euros et gagné le jeu.")
#Jeu terminé