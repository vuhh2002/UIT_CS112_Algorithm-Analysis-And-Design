def getDistance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def solve(point, left, right, res) -> float:
    
    if right - left <= 0:
        return res
    elif right - left == 1:
        return min(res, getDistance(point[left], point[right]))

    mid = left + (right - left) // 2
    res = min(solve(point,left,mid,res), solve(point,mid+1,right,res))

    middleIndex = []
    for i in range(left, right+1):
        if abs(point[i][0] - point[mid][0]) < res:
            middleIndex.append(i)

    for i in range(len(middleIndex)):
        for j in range(i+1, len(middleIndex)):
            res = min(res,
             getDistance(point[middleIndex[i]], point[middleIndex[j]]))

    return res

point = []
for i in range(int(input())):
    x, y = map(int, input().split())
    point.append([x, y])

point.sort(key= lambda x : x[1])
point.sort(key= lambda x : x[0])
res = solve(point, 0, len(point)-1, float('inf'))

print(round(res,3))
