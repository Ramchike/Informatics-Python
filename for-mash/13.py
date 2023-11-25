n = int(input())
sum = 0
for i in range(1, n):
    print(i, end='')
    print('*', end='')
    if i + 1 == n:
        print(i + 1, end='', sep='')
    else:
        print(i + 1, '+', end='', sep='')
    sum += i * (i + 1)
print('=', sum, sep='')