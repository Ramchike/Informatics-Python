numbers = list(map(int, input().split()))
sort = [i for i in numbers if i > 0]
print(min(sort))