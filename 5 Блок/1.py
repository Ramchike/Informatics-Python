max_i = 0
count = 0

for i in range(1012, 9639):
    if i % 3 == 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
        count+= 1
        max_i = max(i, max_i)

print(count, max_i, sep=' ') # 2151 9630