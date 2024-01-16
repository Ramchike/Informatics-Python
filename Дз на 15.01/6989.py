def F(x, y, z):
    return int(x <= (y and z))
print("x y z F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = F(x, y, z)
            if f == 0:
                print(x, y, z, f)
print("2")