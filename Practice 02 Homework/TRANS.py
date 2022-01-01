def bfs(x):
    global E
    dp = {x: 0}
    queue = [x]
    while len(queue) > 0:
        city = queue.pop(0)
        for v in E[city]:
            if v in dp:
                continue
            queue.append(v)
            dp[v] = dp[city] + 1
    return dp

START = 1.0
n, m, k = map(int, input().strip().split(' '))
E = dict()
for i in range(m):
    line = input()
    u, v = map(float, line.strip().split(' '))
    if u not in E:
        E[u] = []
    if v not in E:
        E[v] = []
    E[u].append(v)
    E[v].append(u)

dp = bfs(START)
dp.pop(START)
l = 0
r = 10**18
while l < r:
    mid = l + (r - l) // 2
    total = 0
    for shortest_path in dp.values():
        total += mid // shortest_path
    if total >= k:
        r = mid
    else:
        l = mid + 1

print(l)