MOD = 10**9 + 7
MAX_M = 2 * 10**5
L = MAX_M + 9 + 1
dp = [1] * L
for i in range(10,L):
    dp[i]= (dp[i-9] + dp[i-10]) % MOD
for s in [*open(0)][1:]:
    n, m = s.split()
    m = int(m)
    ans = sum(dp[m + int(c)] for c in n) % MOD
    print(ans)