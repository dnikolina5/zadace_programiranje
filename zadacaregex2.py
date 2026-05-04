'''Napisati regex za provjeru validnosti unosa e-maila.
E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata
ime.prezimeX@sum.ba 
X predstavlja bilo koji broj (moze ici u beskonacnost),
a taj broj ne mora postojati (može biti samo ime.prezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
'''

import re

# regex obrasci
email_regex = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
eduid_regex = r'^[a-zA-Z]+\.[a-zA-Z]+[0-9]*@sum\.ba$'

# unos korisnika
email = input("Unesite email: ")
eduid = input("Unesite eduId: ")

# provjera emaila
if re.match(email_regex, email):
    print("Email je ispravan")
else:
    print("Email nije ispravan")

# provjera eduId
if re.match(eduid_regex, eduid):
    print("eduId je ispravan")
else:
    print("eduId nije ispravan")
