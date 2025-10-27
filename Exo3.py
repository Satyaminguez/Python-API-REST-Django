def roman_to_int(s: str) -> int:
    chiffres_romains = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0 

    # parcours des caractères de la chaîne en ordre inverse
    for char in reversed(s):
        current_value = chiffres_romains[char]

        # Si valeur actuelle est < à la valeur précédente, on soustrait
        if current_value < prev_value:
            total -= current_value
        else:
            # Sinon, on ajoute la valeur actuelle
            total += current_value

        # Mettre à jour la valeur précédente
        prev_value = current_value

    return total

print(roman_to_int("III")) 
print(roman_to_int("IV"))
print(roman_to_int("IX")) 
print(roman_to_int("LVIII")) 
print(roman_to_int("MCMXCIV"))