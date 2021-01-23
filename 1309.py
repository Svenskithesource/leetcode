s = "10#11#12"

l = []
for i in range(0, len(s)):
    if s[i] == "#":
        x = s[i-2] + s[i-1]
        l = l[:len(l)-2]
        l.append(x)
    else:
        l.append(s[i])

print("".join(chr(int(y) + 96) for y in l))