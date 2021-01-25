s = "()[]{}"

brackets = {"(": ")", "{": "}", "[": "]"}
for n, char in enumerate(s):
    if char not in ["}", "]", ")"]:
        continue
    for x in s[n:]:
        print(x, char)
        brackets.pop(brackets[char])
        if x in brackets:
            print(False)
            exit()
        brackets = {"(": ")", "{": "}", "[": "]"}

print(True)
