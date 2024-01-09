import itertools
count = 0
lines = []
with open("9156.txt") as f:
    for b in f:
        lines.append([int(i) for i in b.split()])
for line in lines:
    if (max(line) + min(line)) % 3 == 0:
        line_g = itertools.permutations(line)
        for line_i in line_g:
            if line_i[0] - line_i[1] == line_i[2] - line_i[3]:
                count += 1
                break
print(count)