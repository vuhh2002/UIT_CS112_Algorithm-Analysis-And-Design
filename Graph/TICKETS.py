import heapq

n, m, k = map(int, input().split())

e = [[] for i in range(n + 1)]
d = [[100000000000 for j in range(k + 1)] for i in range(n + 1)]

for i in range(m):
    u, v, w = map(int, input().split())
    e[u].append([w, v])
    e[v].append([w, u])

d[1][0] = 0
heap = [(0, 0, 1)]

while len(heap) > 0:
    du, x, u = heapq.heappop(heap)
    for uv, v in e[u]:
        if d[v][x] > d[u][x] + uv:
            d[v][x] = d[u][x] + uv
            heapq.heappush(heap, (d[v][x], x, v))
        if x < k and d[v][x + 1] > d[u][x]:
            d[v][x + 1] = d[u][x]
            heapq.heappush(heap, (d[v][x + 1], x + 1, v))

print(d[n][k])