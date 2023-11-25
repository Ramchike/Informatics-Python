a, b = map(int, input().split(' '))
for j in range(a + 1, b):
    for i in range(j, b):
        print(a * i * 6)
