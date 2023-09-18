h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())

seconds1 = h1 * 3600 + m1 * 60 + s1
seconds2 = h2 * 3600 + m2 * 60 + s2

dif = seconds2 - seconds1

print(dif)