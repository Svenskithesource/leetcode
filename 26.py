nums = [0,0,1,1,1,2,2,3,3,4]

s = list(set(nums))
for i in range(len(nums)):
    
    try:
        nums[i] = s[i]
    except:
        print(i)
        del nums[i]

print(s)