maxi = 0
count = 0

for i in range(9999, 99999+1):
    sum = 0
    b = i
    while i > 0:
        sum += i%10
        i //= 10
    if b % sum == 0:
        count += 1
        maxi = max(b, maxi)
    
print(count, maxi) #10334 99972