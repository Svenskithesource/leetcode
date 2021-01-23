nums = [8,1,2,2,3]

ans = []
for i in range(0, len(nums)):
    count = 0
    for j in range(0, len(nums)):
        if i != j and nums[j] < nums[i]:
            count += 1
    ans.append(count)

print(ans)