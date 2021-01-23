n = 234

p = int(str(n)[:1])
for x in str(n)[1:]:
    p *= int(x)
s = 0
for y in str(n):
    s += int(y)

print(p-s)