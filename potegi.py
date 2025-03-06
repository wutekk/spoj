def potegi(a, b):
    a = a%10
    c = 1
    for _ in range(b):
        c = c%10
        c = c * a
    return c % 10

t = int(input())
for _ in range(t):
    arg1, arg2 = map(int, input().split(" "))
    print(potegi(arg1, arg2))
    