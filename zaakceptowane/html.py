def jest_mala_litera(litera):
    return (ord(litera) >= ord('a') and ord(litera) <= ord('z'))

def zamiana_na_wielka(litera):
    LiczLitera = ord(litera)
    LiczLitera -= ord('a') - ord('A')
    return chr(LiczLitera)


import sys
for linia in sys.stdin:
    linia = linia.rstrip()
    
    zamieniaj = False
    nowa_linia = ''
    for litera in linia:
        if litera == '>':
            zamieniaj = False

        if zamieniaj == True and jest_mala_litera(litera):
            litera = zamiana_na_wielka(litera)
            
        nowa_linia += litera

        if litera == '<':
            zamieniaj = True
    print(nowa_linia)