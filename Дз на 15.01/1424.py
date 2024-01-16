min_N = 10000000000
for N in range(1000):
    N_bin = bin(N)[2:]
    if int(N_bin) % 2 == 0:
        N_bin += '01'
    else:
        N_bin += '10'