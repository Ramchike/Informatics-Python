# Алгоритм преобразует входное число N> 150 в число R выполняя следующие действия:

# 1. Число N преобразуется в шестнадцатеричную систему счисления;
# 2. В полученной записи все цифры А16 заменяются на 116;
# 3. В полученной записи подсчитывается количество четных цифр, если их больше 2-х, то справа дописывается B16, иначе слева дописывают F16;
# 4. Результат переводится в десятичную систему счисления;

# Определите минимальное значение N для которого получается минимально возможное R большее 3500


min_N = 100000000
min_R = 100000000
arr = []

for i in range(150, 100000):
    N = hex(i)[2:]
    N = N.replace("a", "1")
    
    chet = 0
    
    for j in N: 
        if int(j, 16) % 2 == 0:
            chet += 1 
            
    if chet > 2:
        N += 'b'
    else:
        N = 'f' + N
    
    R = int(N, 16)

    if R > 3500 and R < min_R:
        min_R = min(R, min_R)
        min_N = i

        
print(min_N)
