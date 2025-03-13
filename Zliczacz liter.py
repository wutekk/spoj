
#t = int(input())
#slownik = {}
#for i in range(t):
#    tekst = input()
#    for litera in tekst:
#        if litera == ' ':
#            continue
#        try:
#            slownik[litera] += 1
#        except KeyError:
#            slownik[litera] = 1
#            
#for key in slownik.keys():
#    print(f'{key} {slownik[key]}')


#slownik = {}
#slownik['a'] = 0 # slownik {'a': 0}
#slownik['b'] = 10 # slownik {'a': 0, 'b': 10}

# try:
#    wrazliwy kod
# excpet KLASA_BLEDU:
#   reakcja na blad

t = int(input())
slownik = {}
for i in range(t):
    tekst = input()
    for litera in tekst:
        if litera == ' ':
            continue
        if litera in list(slownik.keys()):
            slownik[litera] += 1
        else:
            slownik[litera] = 1
            
for key in slownik.keys():
    print(f'{key} {slownik[key]}')
