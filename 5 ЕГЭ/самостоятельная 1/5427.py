min_R = 10000000

for N in range(1, 1000):
    N -= bin(N)[2:].count('0')
    
    N_bin = bin(N)[2:]
    N_bin = N_bin[-3:] + N_bin
    
    R = int(N_bin, 2)
    
    if R > 224:
        print(R)
        min_R = min(min_R, R)
        
print(min_R)
    