lst_s = []
count = 0
with open("9740.txt") as f:
    for i in f:
        lst_s.append([int(elem) for elem in i.split()])

def IfRetry3(line: list):
    sort_list = []
    find_i = 0
    for i in line:
        sort_list.append(line.count(i))
    print(line)
    print(sort_list)
    if sort_list.count(3) == 3 and sort_list.count(1) == 6:
        print(line[sort_list.index(3)])
        return line[sort_list.index(3)]
    else:
        return -1

def SumNotRetry(line: list):
    sort_list = []
    for i in line:
        if line.count(i) == 1:
            sort_list.append(i)
    if sum(sort_list) / len(sort_list) < IfRetry3(line):
        return True
    else: return False


for line in lst_s:
    for i in line:
        if line.count(i) == 3 and len(set(line)) == 5:
            i_3 = i
            line.pop(line.index(i))
            if sum(line) / len(line) < i_3:
                count += 1

print(count)

