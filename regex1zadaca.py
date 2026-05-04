'''Potrebno napisati regex koji vraca podudaranje
ukoliko se unese string koji počinje kao prvo slovo vašeg imena,
a završava kao prvo slovo prezimena.
String mora sadržavati bar jedan broj između 0 i 5 i razmak.
'''

import re

regex = r"^N(?=.*[0-5])(?=.*\s).*D$"

tekst = input("Unesi string: ")

if re.match(regex, tekst):
    print("Podudaranje postoji")
else:
    print("Nema podudaranja")
