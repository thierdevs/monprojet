import random
import time

points = 3
tentative = 6
print(f"Bienvenue dans le jeux LET-GET \n")
print(f"####################################\n")
print(f"Vous avez 3 point-erreur\n")
print(f"####################################\n")
print(f"Vous avez 6 tentatives\n")
print("{:^30}\n\n\n".format('+---+---------------+'))
ent = 0
while ent < 1 or ent > 3:
    entre = input("Choisir un niveau de 1 a 3: ")
    ent = int(entre)

print(f"\n\n####################################\n")

print(f"Vous avez choisi le niveau {ent}\n")

liste = ""
niveau1 = []
niveau2 = []
niveau3 = []

with open("mots.txt", "r") as asef:
   var = asef.readlines()
   for ligne in var:
       liste = ligne.replace("\n", "")
       if len(liste) >= 2 and len(liste) <= 4:
           niveau1.append(liste)
       elif len(liste) >= 5 and len(liste) <= 7:
           niveau2.append(liste)
       else:
           niveau3.append(liste)

#print(niveau1)
ch = ''
#niveau1
if ent == 1:
     print("Chargement des données...")
     print(f"{len(niveau1)} mots chargés")

     chercher = random.choice(niveau1)
     print(f"Je vous propose un mot de {len(chercher)} lettres. De quel mot s'agit-il ?")
     print("###############################")
     ch = ch + '_' *len(chercher)
     cher = list(ch)
     print(ch)
     t = time.time()
     while 1:
         print(f"{chercher}")
         lettre = str(input("Saisir une lettre :"))
         if lettre in chercher and cher:
             print("Bravo lettre trouver !")
             i = 0
             chercher1 = list(chercher)
             for vr in chercher1:
                 if vr == lettre:
                     cher[i] = lettre
                 i = i + 1
             print(f"{''.join(cher)}")
             tentative = tentative + 1

         if (lettre == '0' or lettre == '1' or lettre == '2' or lettre == '3' or lettre == '4' or lettre == '5' or lettre == '6' or lettre == '7' or lettre == '8' or lettre == '9'):
             print("Tu ne doit saisir que des lettres de l'alphabets !")
             points = points - 1
             if points  <= 0:
                 tentative = tentative - 1
             print(f"{''.join(cher)}")
         if not(lettre in chercher and cher):
             print("oups lettre raté !")
             points = points - 1
             if points  <= 0:
                 tentative = tentative - 1
             print(f"{''.join(cher)}")
         if tentative <= 0:
             print("Vous navez aucune tentative ")
             print(f"Le mot secret est {chercher}")
             break
         if time.time()-t > 15:
             print("Temps écouler !!!")
             print(f"Le mot secret est {chercher}")
             break
         if chercher == ''.join(cher):
             print("Vous avez gagner Félicitation !!!")
             break
         #print(f"tentative == {tentative}")

     with open("log_game.txt", "w") as var:
         var.write(f"numéro de la partie : {ent}")
         var.write(f"nombres de tentatives : {tentative}")
         var.write(f"score : {tentative * len(chercher)}")


elif ent == 2:
     print("Chargement des données...")
     print(f"{len(niveau2)} mots chargés")

     chercher = random.choice(niveau2)
     print(f"Je vous propose un mot de {len(chercher)} lettres. De quel mot s'agit-il ?")
     print("###############################")
     ch = ch + '_' *len(chercher)
     cher = list(ch)
     print(ch)
     t = time.time()
     while 1:
         #print(f"{chercher}")
         lettre = str(input("Saisir une lettre :"))
         if lettre in chercher and cher:
             print("Bravo lettre trouver !")
             i = 0
             chercher1 = list(chercher)
             for vr in chercher1:
                 if vr == lettre:
                     cher[i] = lettre
                 i = i + 1
             print(f"{''.join(cher)}")
             tentative = tentative + 1

         if (lettre == '0' or lettre == '1' or lettre == '2' or lettre == '3' or lettre == '4' or lettre == '5' or lettre == '6' or lettre == '7' or lettre == '8' or lettre == '9'):
             print("Tu ne doit saisir que des lettres de l'alphabets !")
             points = points - 1
             if points  <= 0:
                 tentative = tentative - 1
             print(f"{''.join(cher)}")
         if not(lettre in chercher and cher):
             print("oups lettre raté !")
             points = points - 1
             if points  <= 0:
                 tentative = tentative - 1
             print(f"{''.join(cher)}")
         if tentative <= 0:
             print("Vous navez aucune tentative ")
             print(f"Le mot secret est {chercher}")
             break
         if time.time()-t > 30:
             print("Temps écouler !!!")
             print(f"Le mot secret est {chercher}")
             break
         if chercher == ''.join(cher):
             print("Vous avez gagner Félicitation !!!")
             break
        # print(f"tentative == {tentative}")
        # print(''.join(cher))

     with open("log_game.txt", "w") as var:
         var.write(f"numéro de la partie : {ent}")
         var.write(f"nombres de tentatives : {tentative}")
         var.write(f"score : {tentative * len(chercher)}")

else:
     print("Chargement des données...")
     print(f"{len(niveau3)} mots chargés")

     chercher = random.choice(niveau3)
     print(f"Je vous propose un mot de {len(chercher)} lettres. De quel mot s'agit-il ?")
     print("###############################")
     ch = ch + '_' *len(chercher)
     cher = list(ch)
     print(ch)
     t = time.time()
     while 1:
         #print(f"{chercher}")
         lettre = str(input("Saisir une lettre :"))
         if lettre in chercher and cher:
             print("Bravo lettre trouver !")
             i = 0
             chercher1 = list(chercher)
             for vr in chercher1:
                 if vr == lettre:
                     cher[i] = lettre
                 i = i + 1
             print(f"{''.join(cher)}")
             tentative = tentative + 1

         if (lettre == '0' or lettre == '1' or lettre == '2' or lettre == '3' or lettre == '4' or lettre == '5' or lettre == '6' or lettre == '7' or lettre == '8' or lettre == '9'):
             print("Tu ne doit saisir que des lettres de l'alphabets !")
             points = points - 1
             if points  <= 0:
                 tentative = tentative - 1
             print(f"{''.join(cher)}")
         if not(lettre in chercher and cher):
             print("oups lettre raté !")
             points = points - 1
             if points  <= 0:
                 tentative = tentative - 1
             print(f"{''.join(cher)}")
         if tentative <= 0:
             print("Vous navez aucune tentative ")
             print(f"Le mot secret est {chercher}")
             break
         if time.time()-t > 45:
             print("Temps écouler !!!")
             print(f"Le mot secret est {chercher}")
             break
         if chercher == ''.join(cher):
             print("Vous avez gagner Félicitation !!!")
             break
        # print(f"tentative == {tentative}")

     with open("log_game.txt", "w") as var:
         var.write(f"numéro de la partie : {ent}")
         var.write(f"nombres de tentatives : {tentative}")
         var.write(f"score : {tentative * len(chercher)}")









