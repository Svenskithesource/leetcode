s = "Hello World"

x = s.split(" ")[::-1]

try:
    print(len([w for w in x if w][0]))
except:
    print(0)
