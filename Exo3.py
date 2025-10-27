# On demande à l'utilisateur d'entrer un chiffre romain
s = input("Entrez un chiffre romain : ").upper()

# Dictionnaire associant chaque symbole romain à sa valeur
valeurs = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Variable pour stocker le résultat final
total = 0

# Parcours de chaque caractère sauf le dernier
for i in range(len(s) - 1):
    # Si la valeur actuelle est plus petite que la suivante, on la soustrait
    if valeurs[s[i]] < valeurs[s[i + 1]]:
        total -= valeurs[s[i]]
    # Sinon, on l'ajoute
    else:
        total += valeurs[s[i]]

# On ajoute la valeur du dernier caractère (toujours positive)
total += valeurs[s[-1]]

# Affichage du résultat
print("Le nombre entier est :", total)
