# Solution gets declined because it exceeds time limit...

n = 6
k = 2

out = [num for num in range(10 ** (n - 1), (10 ** n)) if
       all([abs(int(str(num)[x]) - int(str(num)[x + 1])) == k for x in range(0, n - 1)])]

print(out)
