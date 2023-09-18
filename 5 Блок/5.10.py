numbers = list(map(int, input().split()))

for i in range(1, numbers[0]):
    if numbers[i] > numbers[i-1]:
        print(numbers[i], end=' ')