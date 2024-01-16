min_R = 1000000000
for N in range(1000):
    N_bin = bin(N)[2:]
    N_bin += str(N_bin.count('1') % 2)
    N_bin += str(N_bin.count('1') % 2)
    R = int(N_bin, 2)
    if R > 396:
        min_R = min(R, min_R)
print(min_R)
