N,M = map(int,input().split())
prefix_sum = [0]
for _ in range(N):
    num = int(input())
    prefix_sum.append(prefix_sum[-1] + num)

dp = [[0  for i in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(1,M+1):
        dp[i][j] = -float('inf')
dp[1][1] = prefix_sum[1]

for idx1 in range(2,N+1):
    for idx2 in range(1,M+1):
        dp[idx1][idx2] = dp[idx1-1][idx2]
        if idx2 == 1:
            dp[idx1][idx2] = max(dp[idx1][idx2],prefix_sum[idx1])
        for k in range(idx1-2,-1,-1):
            dp[idx1][idx2] = max(dp[idx1][idx2], dp[k][idx2-1]+ prefix_sum[idx1] - prefix_sum[k+1])
print(dp[N][M])