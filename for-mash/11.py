def factorial(b):
    factor = 1
    for i in range(1, b + 1):
        factor *= i
    return factor

n = int(input())
k = int(input())
print(factorial(n) // (factorial(k) * factorial(n - k)) )