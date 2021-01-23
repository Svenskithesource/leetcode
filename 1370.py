s = "aaaabbbbcccc"

ans = ""
l = []
for i in range(0, len(s)):
    l.append(ord(s[i]))
l = list(dict.fromkeys(l))
j = l

for x in range(0, len(l)):
    ans += chr(min(l))
    l.remove(min(l))

l = j
for x in range(0, len(l)):
    print(chr(max(l)))
    ans += chr(max(l))
    l.remove(max(l))

print(ans)

