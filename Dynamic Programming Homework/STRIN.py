n = int(input())
MOD = 1000000007
dp = [[0, 0, 0] for i in range(100001)]
dp[1][0] = dp[1][1] = dp[1][2] = 1

for i in range (2, n + 1):
  for j in range (3):
    dp[i][j] += dp[i - 1][0]
    if j != 1: dp[i][j] += dp[i - 1][1]
    dp[i][j] += dp[i - 1][2]
    dp[i][j] %= MOD

print((dp[n][0] + dp[n][1] + dp[n][2]) % MOD)