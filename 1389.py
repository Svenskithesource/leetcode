nums = [0,1,2,3,4]
index = [0,1,2,2,1]

target = []
for x in range(0, len(nums)):
    target.insert(index[x], nums[x])
print(target)