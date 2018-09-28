titre = "Jour 2 \n Afficher le labyrinthe à l'aide d'une fonction"
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

affiche_labyrinthe(niveau_1)

