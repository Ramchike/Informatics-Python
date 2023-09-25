
string = ''
a = 5000
count = 0

while a > 0:
    string+= str(a % 5)
    a //= 5
    count+= 1
    
print(string[-2:])