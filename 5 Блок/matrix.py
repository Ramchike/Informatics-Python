n = int(input())
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1:
            matrix[i][j] == 1
        else:
            matrix[i][j] = 0

for i in matrix:
    print(i)
