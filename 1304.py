n = 5

l = []
for i in range(0, n):
    if i == 2:
        l.append(-1)
        l.append(1)
        break
    elif i == n-2:
        l.append(-1)
    elif i == n-1:
        l.append(1)

    else:
        l.append(0)

print(l)