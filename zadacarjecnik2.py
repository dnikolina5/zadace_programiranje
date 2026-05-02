'''Koristeći listu imena iz prethodnog zadatka svakom studentu
generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)'''

imena = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", "Magdalena", "Ivana", "Stipe", "Emanuel", "Petar", "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana", "Marija", "Nikolina", "Andrija", "Slaven", "Sebastian", "Marko", "Frano", "Stipan", "Eugen", "Toni", "Dražan", "Matej", "Nives", "Nemanja", "Sara", "Ružica", "Gabrijel", "Darian", "Ivana", "Ivan Stjepan", "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante", "Josip", "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko", "Sergej", "Matej", "Marin", "Sara", "Josip", "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko", "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", "Petar", "Emanuel", "Helena", "Antonio", "Petar"]

import random

ocjene = {}
broj_ocjena = {1:0, 2:0, 3:0, 4:0, 5:0}
prolazni = 0

for ime in imena:
    ocjena = random.randint(1,5)
    ocjene[ime] = ocjena

    broj_ocjena[ocjena] += 1

    if ocjena > 1:
        prolazni += 1

print("Ocjene studenata")
for ime in ocjene:
    print(ime, ocjene[ime])

print("Broj ocjena")
for ocjena in broj_ocjena:
    print(ocjena, broj_ocjena[ocjena])

print("Postotak prolaznosti:", round(prolazni / len(imena) * 100, 2), "%")
