min_N = 1000000

for N in range(1000):
    N_bin = bin(N)[2:]
    N_bin += str(N_bin.count('1') % 2)
    N_bin += N_bin[-1]
    
    R = int(N_bin, 2)
    
    if R > 60:
        min_N = min(min_N, N)
        
print(min_N)