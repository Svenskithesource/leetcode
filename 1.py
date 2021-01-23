nums = [3,2,3]
target = 6

for nx, x in enumerate(nums):
    for ny, y in enumerate(nums):
        if x+y == target and nx != ny:
            break
    else:
        continue
    break

print([nx, ny])