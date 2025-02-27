def zamienianie_na_wieksza(litera):
    numer_lit = ord(litera)
    numer_lit -= 32
    return chr(numer_lit)

text = input()
nowyText = ''

for i in range(len(text)):
    if text[i] != '_':
        if text[i-1] == '_':
            nowyText += zamienianie_na_wieksza(text[i])
        else: 
            nowyText += text[i]
print(nowyText)