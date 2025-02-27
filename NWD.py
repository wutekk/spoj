
def NWD(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
t = int(input())
for _ in range(t):
    # wejscie = input().split(" ")
    # d = int(wejscie[0])
    # e = int(wejscie[1])
    d, e = map(int, input().split(" ")) # robi to samo co 3 liniki powyzej
    print(NWD(d, e))