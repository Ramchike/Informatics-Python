max_N = 0

def system3(N):
    N_3 = ""
    
    while N:
        N_3 += str(N % 3)
        N //= 3
        
    return N_3[::-1]

for N in range(1, 1000):
    N_3 = system3(N)
    
    if int(N_3) % 3 == 0:
        N_3 = '1' + N_3 + "02"
    else:
        N_3 += system3(int(N_3) % 3 * 4)
   
    R = int(N_3, 3)
    
    if R < 199:
        max_N = max(max_N, N)
print(max_N)
    
