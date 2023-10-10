max_ = 0
count = 0

for b in range(1111, 9999+1):
    sum = 0
    prz = 1
    i = b

    
    while i > 0:
        prz *= i % 10
        sum += i % 10
        i //= 10
    
    if prz == 0:
        prz=1
    elif b % prz == 0 and b % sum == 0:
        count += 1
        max_ = max(max_, b)
        
print(count, max_)