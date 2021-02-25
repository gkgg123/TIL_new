dp = 31*[0]
dp[1] = 1
dp[0] = 1


for n in range(2,31):
    for i in range(n):
        dp[n] += dp[i]*dp[n-i-1]

while True:
    N = int(input())
    if not N:
        break
    print(dp[N])

