valeur_temperature = float(input("Température à convertir : "))

grandeur = input("Choisir la grandeur physique (C pour Celsius, F pour Fahrenheit) : ").upper()

if grandeur == "F":
    # Conversion de Fahrenheit vers Celsius
    celsius = (valeur_temperature - 32) * 5/9
    print("La température en Celsius est de", round(celsius, 2), "degrés.")
elif grandeur == "C":
    # Conversion de Celsius vers Fahrenheit
    fahrenheit = (valeur_temperature * 9/5) + 32
    print("La température en Fahrenheit est de", round(fahrenheit, 2), "degrés.") #round() arrondit à 2 chiffres après la virgule
else:
    print("Unité non reconnue. Veuillez entrer 'C' ou 'F'.")