MOD = 132864579

def fibonacci(i):
    if i <= 1:
        return 1
    a = 1
    b = 1
    for i in range(2, i+1):
        b = (b + a) % MOD
        a = (b - a) % MOD
    return b

a = int(input())
a = list(map(int, input().split()))
for i in a:
    print(fibonacci(i), end=' ')
