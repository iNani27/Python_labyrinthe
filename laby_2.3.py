titre = "Jour 2 \n Afficher le labyrinthe à l'aide d'une fonction aux valeurs transmises sous forme de paramètre"
print(titre)

niveau_1 = [
	"+----------------------------------------+",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"|                                        |",
	"+----------------------------------------+"
]

def affiche_labyrinthe(laby):
  for ligne in laby:
	  print(ligne)

#affiche_labyrinthe(niveau_1)

def affiche_bordures_labyrinthe(taille):
	print("+{}+".format("-" * (taille-2))) # - les 2 coins de la 1ière ligne

	for i in range (taille//2-2):
		print(
      "|{}|".format(" " * (taille-2)) 
      ) 
	#Ci-dessus artifice de calcul car la largeur des - vaut la moitié de la hauteur des | et en python pour obtenir le résultat sans virgule d'une disvision c'est //

  # /	Diviser
  # //	Résultat entier d'une division

	print("+{}+".format("-" * (taille-2))) 	# - les 2 coins de la dernière ligne
	

def choix_joueur():
	return input("Votre déplacement (Haut/Bas/Gauche/droite) ? ")
	

affiche_bordures_labyrinthe(20)

dep=choix_joueur()
print(dep)
	