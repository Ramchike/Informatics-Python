max_i = 0
sum = 0

for i in range(2807, 8558+1):

    if i % 2 == 1 and i // 2 % 2 == 1 and i % 9 == 5:
        max_i = max(i, max_i)
        sum+= i

print(max_i, sum)