max_R = 0

def punkt2(N_bin):
    
    if N_bin.count('1') % 2 == 0:
        N_bin += "00"
        N_bin[:2] == '11'
    else:
        N_bin += "11"
        N_bin[:2] == '10'
        
    return N_bin

for N in range(100):
    N_bin = bin(N)[2:]
    
    N_bin = punkt2(N_bin)
    N_bin = punkt2(N_bin)
    
    R = int(N_bin, 2)
    max_R = max(R, max_R)
    
print(max_R)

        