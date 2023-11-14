string = input()
num = ''
sorted = ''

for i in string:
    if i.isdigit():
        num += i
    else:
        if num == '':
            sorted += i * 1
        else: sorted += i * int(num)
        num = ''
        

for i in range(len(sorted)):
    if i >= 40 and i % 40 == 0:
        print('')
    print(sorted[i], end='')
    