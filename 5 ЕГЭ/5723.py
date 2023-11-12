count_R = 0

for N in range(1, 1000):
    N_bin = bin(N)[2:]
    if N_bin.count('1') % 2 == 0:
        N_bin = "10" + N_bin + "11"
    else:
        N_bin = "11" + N_bin + "11"
    
    R = int(N_bin, 2)
    
    if R < 860:
        count_R += 1
        
print(count_R)