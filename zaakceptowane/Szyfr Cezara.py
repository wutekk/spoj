def cezar(linia):
    wynik = ''
    for literka in linia:
        num =  ord(literka)
        if num >= ord('A') and num <= ord('Z'):
            if num in [ord('Z'), ord('X'), ord('Y')]:
                num -= 26
            num += 3
        wynik += chr(num)
    return wynik

# Odczytanie i przetwarzanie linii po linii
import sys
for linia in sys.stdin:
    print(cezar(linia.rstrip()))  # Usuwa zbędne \n na końcu każdej linii

# z -> c
# z -> a-1 -> a-1 + 3 = c
# z - 26 + 3 -> z - 23
# y - 26 + 3 = b

# if xyz || XYZ 
    # -26