n = int(input())
hour = n // 60 % 24
min = n % 60
print("{:02d}:{:02d}".format(hour, min))