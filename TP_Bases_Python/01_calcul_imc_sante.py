"""
On souhaite calculer l'Indice de Masse Corporelle d'un Patient (IMC)

Ce script utilise des types flottants (float) pour calculer l'IMC d'un patient
à partir de son poids et de sa taillen en appliquant les priorités opératoires
"""

# Voici le poids et la taille d'un patient
poids = 75.5
taille = 1.75
 
# On calcule l'IMC du patient
IMC = poids / taille**2
 
# On affiche le résultat de l'IMC du patient
print(IMC)

