nombres = (55, 42, 948, 116, 309, 1, -43, 60, -459, 1000)

pairs = 0
impairs = 0

for n in nombres:
    if n % 2 == 0:
        pairs += 1
    else:
        impairs += 1

print("Nombre de nombres pairs :", pairs)
print("Nombre de nombres impairs :", impairs)
