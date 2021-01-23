nums = [1,2,3,4,4,3,2,1]
n = 4

res = []
l = len(res)
i = 0
while l != len(nums):
    res.append(nums[i])
    res.append(nums[n + i])
    i += 1
    l += 2

print(res)