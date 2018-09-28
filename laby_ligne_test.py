titre = "Jour 3 Afficher la position [colonne, ligne] du personnage via test entre 2 valeurs \n + Boolean\n\n  Afficher le labyrinthe à l'aide d'une fonction aux valeurs transmises sous forme de paramètre \n et \n Gérer les déplacements entrés par le joueur à l'aide de ... \n\n\n"
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

perso = "X"
position_perso = [1,6]
print(perso)

def affiche_labyrinthe(laby,position_perso):

  n_ligne = 0
  
  for ligne in laby :
    if position_perso[1] == n_ligne :
	    print(ligne, "<- ligne du personnage = ",n_ligne)
    else :
      print(ligne)
    n_ligne = n_ligne + 1

affiche_labyrinthe(niveau_1,position_perso)