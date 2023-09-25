max_i = 0
count = 0

for i in range (1305, 14063+1):
    if i % 2 == 0 or i % 3 == 0 and( i % 7 != 0 and i % 11 != 0 and i % 17 != 0 and i % 23 != 0):
        count+= 1
        max_i = max(max_i, i)
        
print(max_i, i, sep=' ')