for i in range(1, 15):
    print(f'{i%2}: {(9 ** i)%10}')

# 4**b
b = int(input())
print(f'ostatnia cyfra 7^{b} to:')
if b % 2 == 1:
    print(1)
if b % 2 == 0:
    print(9)
if b % 4 == 3:
    print(2)
if b % 4 == 0:
    print(6)
