def ma_liste_de_nombres(lst):
    # On part du dernier chiffre, c'est donc celui ci qui sera changer
    for i in range(len(lst) - 1, -1, -1):
        # ajout de 1 au chiffre actuel
        lst[i] += 1

        # si le chiffre devient 10, on met 0 et on continue la retenue
        if lst[i] == 10:
            lst[i] = 0
        else:
            # si pas de retenue nécessaire, on stop
            break
    # Si encore une retenue apres parcous du tab
    else:
        # Exemple : [9,9,9] devient [1,0,0,0]
        lst.insert(0, 1)

    return lst

user_input = input("Entrez une liste de chiffres séparés par des espaces : ")
# Convertir l'entrée utilisateur en une liste d'entiers
numbers = list(map(int, user_input.split()))

print(ma_liste_de_nombres(numbers))