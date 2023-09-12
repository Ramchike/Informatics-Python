sec = int(input()) % 60
min = sec // 60 % 60
hour = min // 60 % 24
day = hour // 24 % 30
mon = day // 30 % 365
year = day // 365 

print("года: ",  year, ", ", "месяца: ", mon, ", ",  "сутки: ", day, ", ", "часы: ", hour, ", ", "минуты: ", min, ", ",  "секунды: ", sec, sep='')