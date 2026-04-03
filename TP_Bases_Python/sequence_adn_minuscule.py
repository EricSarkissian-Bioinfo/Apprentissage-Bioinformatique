"""
On souhaite à partir d'une séquence ADN donné à quel type correspond
cette séquence pour ensuite mettre la séquence ADN en minuscule

"""

# On souhaite créer une variable sequence_adn avec ATGCGTAC
sequence_adn = 'ATGCGTAC'
print(sequence_adn)

# On souhaite savoir à quel type correspond 'ATGCGTAC'
print(type(sequence_adn))

# On souhaite vérifier si 'ATGCGTAC' correspond bien au type 'str'
print(isinstance(sequence_adn, str))

# On souahaite écrire en minusucle la séquence ADN
print(sequence_adn.lower())
