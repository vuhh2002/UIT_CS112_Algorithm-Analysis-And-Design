# Code nay co tham khao code cua hieult va Trung Kien
# https://oj.vnoi.info/problem/dtdoi/editorial

n, s = list(map(int, input().split()))
denomination = list(map(int, input().split()))
denomination.sort()

res = (s - (2000 - denomination[n-1])) // denomination[n-1]
if res < 0:
    res = 0
money = s - res * denomination[n - 1]

numOfCoin = [float('inf') for i in range(2000)]
numOfCoin[0] = 0
for m in range(1, money+1):
    for i in range(n):
        if m >= denomination[i]:
            numOfCoin[m] = min(numOfCoin[m], numOfCoin[m - denomination[i]] + 1)
        else:
            break

res += numOfCoin[money]
print(res)