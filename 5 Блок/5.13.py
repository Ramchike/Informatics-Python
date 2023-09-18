numbers = list(map(int, input().split()))
sort = [i for i in numbers if i > 0 and i % 2 != 0]

if sort == []:
    print("NO")
else:
    print(min(sort))