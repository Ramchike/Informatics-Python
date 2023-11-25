max_N = 0
def to_9(n):
    str_b = ''
    while n:
        str_b += str(n % 9)
        n //= 9
    return str_b[::-1]

def find_max_count(n):
    counts = []
    for i in range(10):
        counts.append(n.count(str(i)))
    return counts.index(max(counts))

def second_step(n):
    if n.count('5') == n.count('7'):
        n += n[-1]
        return n
    else:
        return n + str(find_max_count(n))

for N in range(1, 10000):
    N_9 = to_9(N)
    for _ in range(4):
        second_step(N_9)
    R = hex(int(N_9))
    if 'BAC' in R:
        max_N = max(max_N, N)

print(max_N)

print(find_max_count('555666777'))