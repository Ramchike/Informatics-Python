max_N = 0
for N in range(1000):
    N_bin = bin(N)[2:]
    if not N % 3:
        N_bin += N_bin[-3:]
    else:
        N_bin += bin(N % 3 * 3)[2:]    
    R = int(N_bin, 2)
    if R < 100:
        max_N = max(max_N, N)
print(max_N)