import random
import time
import fonction
from fonction import *

points = 3
tentative = 6

ent = choixNiveau()


#print(niveau1)

#niveau1
if ent == 1:
     niveau1 = chargementNiveau1()
     print("Chargement des données...\n")
     print(f"{len(niveau1)} mots chargés\n")

     chercher = random.choice(niveau1)
     traitement(chercher, tentative, points, ent)

#print(niveau 2)

elif ent == 2:
     niveau2 = chargementNiveau2()
     print("Chargement des données...\n")
     print(f"{len(niveau2)} mots chargés")

     chercher = random.choice(niveau2)
     traitement(chercher, tentative, points, ent)

#print(niveau 3)

else:
     niveau3 = chargementNiveau3()
     print("Chargement des données...\n")
     print(f"{len(niveau3)} mots chargés")

     chercher = random.choice(niveau3)
     traitement(chercher, tentative, points, ent)
