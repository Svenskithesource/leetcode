s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

shuffled = ""

for x in range(0, len(indices)):
    shuffled += s[indices.index(x)]

print(shuffled)