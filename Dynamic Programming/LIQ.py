def liq(n, a):
    table = [1] * n
    for j in range(1,n):
        for i in range(j-1, -1, -1):
            if a[j] > a[i]:
                table[j] = max(table[j], table[i] + 1)
    for j in range(1,n):
        table[j] = max(table[j], table[j-1])
    return table[n-1]

n = int(input().strip())
a = list(map(int, input().strip().split()))
print(liq(n, a))