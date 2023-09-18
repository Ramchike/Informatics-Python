numbers = list(map(int, input().split()))
para = False

for i in range(1, numbers[0]):
    if numbers[i] > 0 and numbers[i+1] > 0:
        print(numbers[i], numbers[i+1], sep=' ', end=' ')
        para = True
        break

if para == False:
    print("NO")

    