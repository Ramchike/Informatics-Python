n = int(input())
n_new = 10000000
for _ in range(n):
    enter = int(input())
    if enter < n_new and not enter % 2:
        n_new = enter
print(n_new)