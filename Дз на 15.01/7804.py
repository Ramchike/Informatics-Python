def F(x, y, z, w):
    return (not (y <= z)) or ((not x) <= (not w)) or x
print("x y z w F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = F(x, y, z, w)
                if f == 0:
                    print(x, y, z, w, f)
print("ywzx")