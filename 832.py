A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]


for i in range(0, len(A)):
    A[i] = A[i][::-1]
for j in A:
    for x in range(0, len(j)):
        j[x] = 0 if j[x] == 1 else 1

print(A)