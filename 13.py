s = "MCMXCIV"

roman = {"I": 1, "V": 5,"X": 10, "L": 50, "C": 100, "D": 500,"M": 1000}

n = 0
for r in range(len(s)):
    t = roman[s[r]]
    p = roman[s[r-1]]
    if t > p:
        if t == 1 and p in [5, 10]:
            n -= p
            n += p-t
        elif t == 5 and p in [50, 100]:
            n -= p
            n += p-t
        elif t == 100 and p in [500, 1000]:
            n -= p
            n += p-t
    else:
        n += roman[s[r]]
print(n)