nums = [3,4,5,2]

l = []

for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if i != j:
            l.append((nums[i]-1)*(nums[j]-1))

print(max(l))


