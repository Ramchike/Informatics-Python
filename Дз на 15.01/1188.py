min_R = 1000000
for N in range(1000):
    N_bin = bin(N)[2:]
    if not N % 2:
        N_bin += N_bin[-2:]
    else:
        N_bin = '1' + N_bin + '1'
    R = int(N_bin, 2)
    if R > 130:
        min_R = min(R, min_R)
print(min_R)
