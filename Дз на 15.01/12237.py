max_N = 0
for N in range(1000):
    N_bin = bin(N)[2:]
    if N % 2 == 0:
        N_bin += N_bin[-2:]
    else:
        N_bin = '1' + N_bin + '0'
    R = int(N_bin, 2)
    if R < 100:
        max_N = max(N, max_N)
print(max_N)