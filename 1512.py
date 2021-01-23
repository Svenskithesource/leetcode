nums = [1,2,3,1,1,3]


ans = 0
for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if nums[i] == nums[j] and i < j:
            ans += 1

print(ans)
