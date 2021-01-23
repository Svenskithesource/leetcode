s = "RLRRLLRLRL"

count = 0
lCount = 0
rCount = 0

for c in s:
    if c == 'L':
        lCount += 1
    else:
        rCount += 1

    if lCount == rCount:
        count += 1
        lCount = 0
        rCount = 0

print(count)