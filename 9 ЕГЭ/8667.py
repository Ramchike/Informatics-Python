lst_s = []
count = 0

with open("8667") as f:
    for i in f:
        lst_s.append([int(elem) for elem in i.split()])

def algo(line: list):
    summ_3_5 = (max(line) + min(line)) * 5
    line.pop(line.index(min(line)))
    line.pop(line.index(max(line)))
    sum_4 = sum(line) * 3
    return summ_3_5 >= sum_4

for line in lst_s:
    if len(set(line)) == len(line) and algo(line):
        count += 1
print(count)


