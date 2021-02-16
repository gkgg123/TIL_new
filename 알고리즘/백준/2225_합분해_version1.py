# 2225번 합분해


N,K = map(int,input().split())

dp = [[1]*(N+1) if i==0 else [0]*(N+1) for i in range(K)]


for ind in range(1,K):
    for prev_num in range(N,-1,-1):
        for current_num in range(N,-1,-1):
            if prev_num + current_num <=N:
                dp[ind][prev_num+current_num] += dp[ind-1][prev_num]


print(dp[K-1][N]%1000000000)