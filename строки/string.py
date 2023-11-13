string = input()
num = ''
sorted = ''

for i in string:
    if i.isdigit():
        num += i
    else:
        sorted += int(num) * i
        num = ''
        
print(sorted)