max_i = 0
count = 0

for i in range(1388, 63252+1):
    if i % 12 != 0:
        b = i
        while b > 0:
            if b % 10 == 4 or b % 10 == 7:
                count += 1
                max_i = max(max_i, i)
                break
            b //= 10
print(count, max_i)