count = 0
i_13 = 0
for i in range(2894, 174882+1):
    if i % 10 == 8:
        b = i
        sum = 0
        
        while b > 0:
            sum += b % 10
            b //= 10
            
        if sum > 22:
            count+=1
            if count == 13:
                i_13 = i

            

print(count, i_13)