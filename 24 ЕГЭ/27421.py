max_len = 0

with open(r'C:\Users\user\Desktop\projects\Informatics-Python\24 ЕГЭ\24_demo.txt') as f:
    s = f.read()
    now_len = 1
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            now_len += 1
        else:
            max_len = max(now_len, max_len)
            now_len = 1
    print(max_len)
