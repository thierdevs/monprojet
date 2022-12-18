import random
import time

def choixNiveau(ent = 0):
    print(f"\n\nBienvenue dans le jeux LET-GET \n")
    print(f"####################################\n")
    print(f"Vous avez 3 point-erreur\n")
    print(f"####################################\n")
    print(f"Vous avez 6 tentatives\n")
    print("{:^30}\n\n\n".format('+---+---------------+'))
    
    while ent < 1 or ent > 3:
         entre = input("Choisir un niveau de 1 a 3: ")
         ent = int(entre)

    print(f"\n\n####################################\n")

    print(f"Vous avez choisi le niveau {ent}\n")
    
    return ent
    
# FIN choixNiveau
    
# ################################################################################### #

def chargementNiveau1(niveau1 = []):
    with open("mots.txt", "r") as asef:
        var = asef.readlines()
        for ligne in var:
            liste = ligne.replace("\n", "")
            if len(liste) >= 2 and len(liste) <= 4:
                niveau1.append(liste)
    return niveau1

# FIN chargementNiveau1

# ################################################################################# #

def chargementNiveau2(niveau2 = []):

    with open("mots.txt", "r") as asef:
        var = asef.readlines()
        for ligne in var:
            liste = ligne.replace("\n", "")
            if len(liste) >= 5 and len(liste) <= 7:
                niveau2.append(liste)
    return niveau2

# FIN chargementNiveau2

# ################################################################################# #

def chargementNiveau3(niveau3 = []):

    with open("mots.txt", "r") as asef:
        var = asef.readlines()
        for ligne in var:
            liste = ligne.replace("\n", "")
            if len(liste) > 7:
                niveau3.append(liste)
    return niveau3

# FIN chargementNiveau3

# ################################################################################# #

def traitement(chercher, tentative, points, ent, liste = "", ch = ''):
     print(f"Je vous propose un mot de {len(chercher)} lettres. De quel mot s'agit-il ?\n")
     print("###############################")
     chercher = chercher.lower()
     ch = ch + '_' *len(chercher)
     cher = list(ch)
     print(ch)
     t = time.time()
     while 1:
         #print(f"{chercher}")
         print("\n")
         lettre = str(input("Saisir une lettre :")).lower()
         print("\n")
         
         if (not lettre.isalpha()):
             print("\nTu ne doit saisir que des lettres de l'alphabets !")
             if points  <= 0:
                 tentative = tentative - 1
                 print(f"\nil vous reste {tentative} tentatives \n")
             else:
                 points = points - 1
                 print(f"il vous reste {points} avertissement\n")
                 print("######################################\n")
                 print(f"il vous reste {tentative} tentatives\n")
                 print("######################################\n")
                 
             print(f"{''.join(cher)}")
         
         if lettre in chercher:
             if (lettre not in cher):
                print("Bravo lettre trouver !\n")
                i = 0
                chercher1 = list(chercher)
                for vr in chercher1:
                  if vr == lettre:
                     cher[i] = lettre
                  i = i + 1 
                tentative = tentative + 1
             else:
                 print("Lettre déja trouvé.")
                 print("\n#######################")
                 tentative = tentative - 1
                 print(f"\nil vous reste {points} avertissement\n")
                 print("######################################\n")
                 print(f"il vous reste {tentative} tentatives\n")
                 print("######################################\n")
             
             print(f"{''.join(cher)}")
             

         
         if not(lettre in chercher and cher):
             if not (lettre in "aeiouy"):
                 print("\nVous avez Saisi une consonne qui n'est pas dans le mot. \n")
                 print("Vous perdez une tentative. \n")
                 tentative = tentative - 1
             else:
                 print("\nVous avez Saisi une voyelle qui n'est pas dans le mot. \n")
                 print("Vous perdez deux tentative. ")
                 tentative = tentative - 2
             print("\n############################\n")
             print(f"il vous reste {tentative} tentatives \n")
             print("#############################\n")
             print(f"{''.join(cher)}")
         if tentative <= 0:
             print("\nVous navez aucune tentative \n")
             print(f"Le mot secret est {chercher}\n")
             break
         if time.time()-t > 300:    # qui sont les 5 min ( 5 * 60 )
             print("\nTemps écouler !!!\n")
             print(f"Le mot secret est {chercher}\n")
             break
         if chercher == ''.join(cher):
             print("Vous avez gagner Félicitation !!!")
             break
         #print(f"tentative == {tentative}")

     with open("log_game.txt", "w") as var:
         var.write(f"numéro de la partie : {ent}\n\n")
         if tentative < 0:
             var.write(f"nombres de tentatives : 0\n\n")
             var.write(f"score : 0\n")
         else:
             var.write(f"nombres de tentatives : {tentative}\n\n")
             var.write(f"score : {tentative * len(chercher)}\n")