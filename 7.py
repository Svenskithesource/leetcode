x = 123

m = str(x)[::-1]
if m.endswith("-"):
    m = int("-" + m[:-1])
else:
    m = int(m)
if 2 ** 31 >= m >= -2 ** 31:
    print(m)
else:
    print(0)
