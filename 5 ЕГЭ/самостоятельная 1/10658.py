min_R = 100000

def system3(N):
    N_3 = ""
    
    while N:
        N_3 += str(N % 3)
        N //= 3
        
    return N_3[::-1]
        

for N in range(11, 1000):
    N_3 = system3(N)
    
    if N_3.count('2') + N_3.count('0') > N_3.count('1'):
        N_3 = "22" + N_3
    else:
        N_3 = "11" + N_3
    
    R = int(N_3, 3)
    
    if R > 100: 
        min_R = min(min_R, R)
        
print(min_R)