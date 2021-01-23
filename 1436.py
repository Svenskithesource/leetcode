paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

fir = []
sec = []
for path in paths:
    fir.append(path[0])
    sec.append(path[1])

for x in sec:
    if x not in fir:
        print(x)