max_i = 0
count = 0

for i in range(3201, 12877):
    if i % 4 ==0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0 and i % 19 != 0:
        max_i = max(max_i, i)
        count+= 1
        
print(count, max_i, sep=' ') # 1649 12876