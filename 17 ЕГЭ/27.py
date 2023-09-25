min_i = 8433
count = 0

for i in range(3712, 8432+1):
    if i % 2 == i % 4 and i % 13 == 0 or i % 14 == 0 or i % 15 == 0:
        min_i = min(min_i, i)
        count+= 1
        
print(min_i, count)