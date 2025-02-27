def potegi(a, b):
    c = a ** b
    return c % 10

t = int(input())
for _ in range(t):
    arg1, arg2 = map(int, input().split(" "))
    print(potegi(arg1, arg2))
    