J = "aA"
S = "aAAbbbb"

ans = 0
for x in S:
    if x in J:
        ans += 1

print(ans)