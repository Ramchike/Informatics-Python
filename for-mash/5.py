n = int(input())
w_n = -10000
for _ in range(n):
    enter = int(input())
    if enter > w_n:
        w_n = enter
print(w_n)