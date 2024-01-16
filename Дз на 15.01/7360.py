min_N = 1000000000
for N in range(1000):
    N_bin = bin(N)[2:]
    if len(N_bin) % 2 == 0:
        N_bin = N_bin[len(N_bin) // 2:] + '000' + N_bin[:len(N_bin) // 2]
    else:
        N_bin = '1' + N_bin + '01'
    R = int(N_bin, 2)
    if R > 100:
        min_N = min(N, min_N)
print(min_N)