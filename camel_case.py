text = input()
nowyText = ''
for znak in text:
    if znak != '_':
        nowyText += znak
print(nowyText)