strs = [""]


strs, common = [min(strs), max(strs)], ""
for i in range(len(strs[0])):
    common = strs[0][:-(i - len(strs[0]))] if strs[1].startswith(strs[0][:-(i - len(strs[0]))]) else ""
    if common: break

print(common if common else "")
