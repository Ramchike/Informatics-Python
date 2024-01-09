from itertools import *

print("w", "z", "x", "y", "F")

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                F = (x <= y) and z and not w
                if F == 1:
                    print(w, z, x, y, int(F))


print(*product([0]))