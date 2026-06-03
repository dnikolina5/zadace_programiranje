#Napisati rekurzivnu funkciju koja kao parametar prima string,
#a kao rezultat taj string ispisuje sa zada.

def ispisi_unazad(s):
    if s == "":
        return
    else:
        ispisi_unazad(s[1:])
        print(s[0], end="")
        
ispisi_unazad("python")
