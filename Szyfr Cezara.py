def cezar(linia):
    wynik = ''
    for literka in linia:
        num =  ord(literka)
        if num in [120, 121, 122, 88, 89, 90]:
            num -= 26
        num += 3
        wynik += chr(num)
    return wynik
print(cezar(input()))


# z -> c
# z -> a-1 -> a-1 + 3 = c
# z - 26 + 3 -> z - 23
# y - 26 + 3 = b

# if xyz || XYZ 
    # -26