max_N = 0
for N in range(10000):
    N_4 = N - N % 4
    N_bin = bin(N_4)[2:]
    N_bin += str(N_bin.count('1') % 2)
    N_bin += str(N_bin.count('1') % 2)
    R = int(N_bin, 2)
    if R < 64:
        max_N = max(max_N, N)
print(max_N)