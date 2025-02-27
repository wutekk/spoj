t = int(input())
for i in range(t):
    test = input().split()
    n = int(test[0])
    dane = list(map(int, test[1:]))
    suma = 0
    for elem in dane:
        suma += elem
    srednia = suma / len(dane)
    print(srednia)
    najblizsza = 0
    for elem in dane:
        if abs(srednia - elem) < abs(srednia - najblizsza):
            najblizsza = elem
    print(najblizsza)