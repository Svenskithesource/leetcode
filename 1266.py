points = [[1,1],[3,4],[-1,0]]

res=0
for i in range (len(points)-1):
    print(i)
    x = abs(points[i+1][0] - points[i][0])
    y = abs(points[i+1][1] - points[i][1])
    res+=max(x,y)
print(res)