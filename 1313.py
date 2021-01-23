nums = [1,2,3,4]

ans = []
for x in range(0, int(len(nums)/2)):
    [freq, val] = [nums[2*x], nums[2*x+1]]
    for y in range(0, freq):
        ans.append(val)

print(ans)