t = int(input())
for _ in range(t):                                            
    lista = list(map(int, input().split(" ")))
    n = lista[0]
    lista = lista[1:] 
    for i in range(n):
        if i % 2 == 1: # pozycja parzysta - wpisujemy je najpierw
            print(lista[i],end=' ')
    for i in range(n):
        if i % 2 == 0: # pozycja nieparzysta
            print(lista[i],end=' ')

