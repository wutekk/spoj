def zamienianie_na_wieksza(litera):
    numer_lit = ord(litera)
    numer_lit -= 32
    return chr(numer_lit)

stary_text = input()
nowyText = ''

for i in range(len(stary_text)):
    if stary_text[i] != '_':
        if stary_text[i-1] == '_':
            nowyText += zamienianie_na_wieksza(stary_text[i])
        else: 
            nowyText += stary_text[i]
print(nowyText)