count = 0
max_i = 0

for i in range(333666, 666999+1):
    b = i
    countof7 = 0

    if i % 17 == 0:
        while i > 0:
            if i % 10 == 7:
                countof7 += 1
            i //= 10
        if countof7 >= 2:
            count += 1
            max_i = max(max_i, b)

print(count, max_i)