count = 0
max_i = 0

for i in range(8800, 55535+1):
    razryad = 1
    countof7 = 0
    b = i
    
    while i > 0:
        razryad *= i % 10
        if i % 10 == 7:
            countof7 += 1
        i //= 10
    
    if countof7 >= 1 and razryad > 35:
        max_i = max(max_i, b)
        count += 1
        
print(count, max_i)