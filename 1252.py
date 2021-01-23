n = 2
m = 3
indices = [[0,1],[1,1]]

matrix = []
for x in range(0, n):
    t = []
    for y in range(0, m):
        t.append(0)
    matrix.append(t)

for i in range(0, len(indices)):
    ri, ci = indices[i]
    o = []
    for k in matrix[ri]:
        o.append(k + 1)
    matrix[ri] = o
    print(matrix[ri])
    for z in matrix:
        z[ci] += 1

count = 0
for w in matrix:
    for e in w:
        if e % 2 != 0:
            count += 1

print(count)