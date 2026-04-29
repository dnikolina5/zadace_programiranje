import random

matrica = []
for i in range(7):
    red = []
    for j in range(7):
        broj = random.randint(1, 9)
        red.append(broj)
    matrica.append(red)

for i in range(7):
    for j in range(7):
        print(matrica[i][j], end=" ")
    print()

zbroj = 0
for i in range(7):
    for j in range(7):
        if i == 0 or i == 6 or j == 0 or j == 6:
            zbroj = zbroj + matrica[i][j]

print("Zbroj rubova je:", zbroj)
