num = 9669

l = []
l.append(num)
for x in range(0, len(str(num))):
    if str(num)[x] == "9":
        l.append(int(str(num)[:x] + "6" + str(num)[x+1:]))
    else:
        l.append(int(str(num)[:x] + "9" + str(num)[x+1:]))

print(max(l))