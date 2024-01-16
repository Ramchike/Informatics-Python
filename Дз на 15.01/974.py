min_N = 1000000
for N in range(1000):
    N_bin = bin(N)[2:]
    if len(N_bin) >= 2:
        if N_bin[-1] == N_bin[-2]:
            N_bin += '0'
        else:
            N_bin += '1'
    else:
        N_bin += '0'
    if len(N_bin) >= 2:
        if N_bin[-1] == N_bin[-2]:
            N_bin += '0'
        else:
            N_bin += '1'
    else:
        N_bin += '0'
    R = int(N_bin, 2)
    if R > 93:
        min_N = min(N, min_N)
print(min_N)
