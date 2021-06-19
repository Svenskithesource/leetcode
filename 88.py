nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
m = 6
nums2 = [1, 2, 2]
n = 3

for x in nums1:
    if nums1[0] == 0:
        nums1.pop(0)
    elif nums1[-1] == 0:
        nums1.pop()
    else:
        break

for x in nums2:
    if nums2[0] == 0:
        nums2.pop(0)
    elif nums2[-1] == 0:
        nums2.pop()
    else:
        break

[nums1.append(x) for x in nums2]

print(nums1)

print(nums1)

n = len(nums1)

for i in range(n):
    already_sorted = True

    for j in range(n - i - 1):
        if nums1[j] > nums1[j + 1]:

            nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]

            already_sorted = False

    if already_sorted:
        break


print(nums1)


print(nums1)
