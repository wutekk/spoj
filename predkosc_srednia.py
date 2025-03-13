# v_sr = (s1 + s2) / (t1 + t2)
# t1 = s1/v1      t2 = s2/v2

# s1 == s2
# v_sr = 2s / (s/v1 + s/v2)
# v_sr = 2*v1*v2/((v2 + v1))
ODL_MIAST = 1
try:

    t = int(input())
    for i in range(t):
        lista = list(map(int, input().split(" ")))
        s1 = s2 = ODL_MIAST
        v1 = lista[0]
        v2 = lista[1]

        t1 = s1 / v1 
        t2 = s2 / v2
        suma_s = s1 + s2 
        suma_t = t1 + t2
        wynik = suma_s / suma_t
        wynik = round(wynik)
        # suma drog / suma czasow = wynik
        print(wynik)
except EOFError:
    pass