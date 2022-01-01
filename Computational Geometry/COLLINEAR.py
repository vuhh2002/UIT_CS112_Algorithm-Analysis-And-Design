def solve(n, x, y): 
  res = 0;
  for i in range(2, n):
    a = []
    for j in range(i): 
        dy = y[j] - y[i]
        if (dy != 0): 
            ai = (x[j] - x[i]) / dy
            a.append(ai)
        else:
            a.append(1e9)
    a.sort()
    count = 1;
    for j in range(1, i):
        if (a[j] != a[j-1]):
            res += int(count*(count-1) / 2)
            count = 0
        count += 1
    res += int(count*(count-1) / 2)
  return res

n = int(input())
x = []
y = []
for i in range(n):
    xi, yi =  map(int, input().split())
    x.append(xi)
    y.append(yi)
print(solve(n, x, y))