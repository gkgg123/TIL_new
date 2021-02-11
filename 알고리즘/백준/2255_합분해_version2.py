N,K = map(int,input().split())

dp = [[1]*(N+1) if ind==0 else [0]*(N+1) for ind in range(K)]


for k in range(1,K):
    for num in range(N+1):
        dp[k][num] = (dp[k-1][num] + dp[k][num-1])%1000000000

print(dp[K-1][N])