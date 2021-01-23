startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4

ans = 0
for i in range(0, len(startTime)):
    if queryTime in range(startTime[i], endTime[i] + 1):
        ans += 1

print(ans)