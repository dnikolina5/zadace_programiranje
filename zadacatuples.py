'''Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.

Napraviti novi rječnik gdje će se po bodovnom rangu
upisivati broj ostvarenih ocjena. 

Nedovoljan
0-49%

Dovoljan
50-65%

Dobar
65-80%

Vrlodobar
80-90%

Izvrstan
90-100%
'''

studenti = []

with open("rezultati.csv", "r", encoding="utf-8") as datoteka:
    next(datoteka)

    for red in datoteka:
        podaci = red.strip().split(",")

        ime = podaci[0]
        prezime = podaci[1]
        bodovi = int(podaci[2])

        studenti.append((ime, prezime, bodovi))

def uzmi_prezime(student):
    return student[1]

studenti.sort(key=uzmi_prezime)

ocjene = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlo dobar": 0,
    "Izvrstan": 0
}

for s in studenti:
    bodovi = s[2]

    if bodovi <= 49:
        ocjene["Nedovoljan"] += 1

    elif bodovi <= 65:
        ocjene["Dovoljan"] += 1

    elif bodovi <= 80:
        ocjene["Dobar"] += 1

    elif bodovi <= 90:
        ocjene["Vrlo dobar"] += 1

    else:
        ocjene["Izvrstan"] += 1

print("Sortirani studenti:")
for s in studenti:
    print(s)

print("Ocjene:")
for k in ocjene:
    print(k, ocjene[k])
