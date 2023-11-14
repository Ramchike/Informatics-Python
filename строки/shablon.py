def isvalid(pattern, word):
    if not pattern and not word:
        return True
    if not pattern or not word:
        return False
    if pattern[0] == "*":
      
    for i in range(len(word) + 1):
        if isvalid(pattern[1:], word[i:]):
            return True
        return False

    if pattern[0] == "?":
        return isvalid(pattern[1:], word[1:])

    if pattern[0] == word[0]:
        return isvalid(pattern[1:], word[1:])



  return False


word = input()
pattern = input()

print("YES" if isvalid(pattern, word) else "NO")

