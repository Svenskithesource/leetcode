arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
ans = []

for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        for k in range(0, len(arr)):
            if 0 <= i < j < k < len(arr):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    ans.append((arr[i], arr[j], arr[k]))

print(len(ans))