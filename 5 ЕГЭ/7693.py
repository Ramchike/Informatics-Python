max_N = 0

def sixsys(N):
    n_six = ""
    
    while N:
        n_six += str(N % 6)
        N //= 6
    
    return n_six[::-1]

for i in range(1, 10**5):
    N = sixsys(i)
    N += N[-1]
    N = int(N, 6)
    N = bin(N)[2:]
    R = N.count("1")
    
    if R == 18:
        max_N = max(max_N, i)
        
print(max_N)