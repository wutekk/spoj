suma = 0
try:
    while True:
        skladnik = int(input())
        suma += skladnik
        print(suma)
except EOFError:
    pass