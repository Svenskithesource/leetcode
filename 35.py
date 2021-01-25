nums = [1, 3]
target = 2

if not target:
    print(0)
    exit()
for i in range(len(nums)):
    if nums[i] == target or nums[i] > target or i == len(nums)-1:
        if i == len(nums)-1 and nums[i] < target and target != 1:
            print(i+1)
        else:
            print(i)
        exit()
