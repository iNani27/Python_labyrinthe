import random as rd

nombre = rd.randint(1, 10)
print("Jeu du + OU - ? Devine le nombre auquel je pense, entre 1 et 10")
reponse = 0

while reponse != nombre :
  print("Tape un nombre entier entre 0 et 10")
  reponse =int(input())
  if reponse > nombre :
    print ("C'est moins :-( ")
    
  elif reponse < nombre :
    print ("C'est plus :-(D ")
  
print ("Yes :-) , le nombre =  ", nombre)
  

