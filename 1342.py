num = 14

ans = 0
while num != 0:
    if num % 2 == 0:
        num /= 2
    else:
        num -= 1
    ans += 1

print(ans)