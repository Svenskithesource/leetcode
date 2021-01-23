candies = [2,3,5,1,3]
extraCandies = 3

ans = []
m = max(candies)
for candie in candies:
    if candie + extraCandies >= m:
        ans.append(True)
    else:
        ans.append(False)

print(ans)