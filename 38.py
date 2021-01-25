n = 1211


if n == 1:
    print(1)
    exit()
ans = ""
c = []
for i in range(11):
    k = str(n).count(str(i))
    if k:
        c.append({i: k})

print(c)
# prev = []
# for h in str(n):
#     if h in prev:
#         continue
#     ans += str(int(str(c[int(h)]) + str(h)))
#
#     prev.append(h)
#
# print(ans)