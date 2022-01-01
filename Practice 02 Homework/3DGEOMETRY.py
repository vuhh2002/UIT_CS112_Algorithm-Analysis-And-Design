def dist3D(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)**0.5

# for i in range(1):
#     line = input()
for line in [*open(0)][1:]:
    xA, yA, zA, xB, yB, zB, xC, yC, zC = map(int,line.strip().split())
    A = [xA, yA, zA]
    B = [xB, yB, zB]
    C = [xC, yC, zC]
    dAB = dist3D(A, B)
    dBC = dist3D(B, C)
    dCA = dist3D(C, A)
    p = (dAB + dBC + dCA) / 2
    S = (p*(p-dAB)*(p-dBC)*(p-dCA))**0.5
    ans = 2 * S / dBC
    print("{:.2f}".format(ans))