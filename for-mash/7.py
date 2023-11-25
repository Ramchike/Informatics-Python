n = int(input())
index_s = 0
index_i = 0
n_s = -10000
n_i = 10000

for i in range(1, n+1):
    enter = int(input())
    if enter > n_s:
        index_s = i
        n_s = enter
    if enter < n_i:
        index_i = i
        n_i = enter

print(index_i, index_s)