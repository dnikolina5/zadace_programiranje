def pozdrav(ime):
    return "Pozdrav " + ime + "!"

dobrodosla = lambda ime: "Dobrodošla " + ime + "!"

def ispisi(funkcija, ime):
    print(funkcija(ime))

ispisi(pozdrav, "Nina")

ispisi(dobrodosla, "Nina")
