max_i = 0
count = 0

for i in range(1100, 11000+1):
    if i % 6 == 0 and i % 7 != 0 and i % 13 != 0 and i % 17 != 0 and i % 23 != 0:
        max_i = max(max_i, i)
        count+= 1
        
print(count, max_i, sep=' ') # 1178 10992