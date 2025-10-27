# Parcours de tous les nombres entre 1500 et 2700 inclus
for x in range(1500, 2701):
    # Si le nombre est divisible par 7 ET multiple de 5
    if (x % 7 == 0) and (x % 5 == 0):
        print(x)
