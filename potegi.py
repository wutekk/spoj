def potegi(a, b):
    if a % 10 == 0:
        print(0)
    if a % 10 == 1:
        print(1)
    if a % 10 == 2:
        if b % 4 == 1:
            print(2)
        if b % 4 == 2:
            print(4)
        if b % 4 == 3:
            print(8)
        if b % 4 == 0:
            print(6)
    if a % 10 == 3:
        if b % 4 == 0:
            print(1)
        if b % 4 == 1:
            print(3)
        if b % 4 == 2:
            print(9)
        if b % 4 == 3:
            print(7)
    if a % 10 == 4:
        if b % 2 == 1:
            print(4)
        if b % 2 == 2:
            print(6)
    if a % 10 == 5:
        print(5)
    if a % 10 == 6:
        print(6)
    if a % 10 == 7:
        if b % 4 == 1:
            print(7)
        if b % 4 == 2:
            print(9)
        if b % 4 == 3:
            print(3)
        if b % 4 == 0:
            print(1)
    if a % 10 == 8:
        if b % 4 == 1:
            print(8)
        if b % 4 == 2:
            print(4)
        if b % 4 == 3:
            print(2)
        if b % 4 == 0:
            print(6)
    if a % 10 == 9:
        if b % 2 == 1:
            print(1)
        if b % 2 == 0:
            print(9)

try:
    t = int(input())
    for _ in range(t):
        arg1, arg2 = map(int, input().split(" "))
        print(potegi(arg1, arg2))
except:
    pass # sędzia wrzucał pusty plik na input >:(