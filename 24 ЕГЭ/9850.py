stroka = open("9850").read()
symbols = ['L', 'I', 'S', 'E', 'N', 'O', 'K']
max_len, now_len = 0, 0
for char in stroka:
    if char not in symbols:
        now_len += 1
    else:
        max_len = max(now_len, max_len)
        now_len = 0
print(max_len)
