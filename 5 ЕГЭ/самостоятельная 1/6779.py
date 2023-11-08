min_N = 10000000

for N in range(1000):
    N_bin = bin(N)[2:]
    
    if N_bin.count('1') % 2 == 0:
        N_bin += '0'
        N_bin[:3] == '101'
    else:
        N_bin += "11"
        N_bin[:2] == '10'
    
    R = int(N_bin, 2)
    
    if R > 68:
        min_N = min(min_N, N)
print(min_N)