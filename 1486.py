n = 5
start = 0

nums = []

for x in range(0, n):
    nums.append(start + 2*x)
p = nums[0]
for y in nums[1:]:
    p ^= y

print(p)