def ispisi_unazad(s):
    if s == "":
        return
    else:
        ispisi_unazad(s[1:])
        print(s[0], end="")
        
ispisi_unazad("")
