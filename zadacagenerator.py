#Napraviti generator funkcije za
#ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra

def generator_parni_neparni(n):
    for i in range(n):
        if i % 2 == 0:
            yield ("parni", i)
        else:
            yield ("neparni", i)

broj = 10

for tip, vrijednost in generator_parni_neparni(broj):
    print(tip, vrijednost)

