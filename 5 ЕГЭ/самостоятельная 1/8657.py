max_N = 0

def system3(N):
    N_3 = ""
    while N:
        N_3 += str(N % 3)
        N //= 3 
    return N_3[::-1]

for N in range(1, 1000):
    N_3 = system3(N)
    
    if N % 5 == 0:
        N_3 += N_3[-3:]
    else:
        N_3 += system3(N % 5 * 5)
    
    R = int(N_3, 3)
    
    if R < 5496:
        max_N = max(max_N, N)
        
print(max_N)    
