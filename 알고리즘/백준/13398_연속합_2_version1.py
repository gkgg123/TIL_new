N = int(input())

arr = list(map(int,input().split()))
minus_inf = -float('inf')
dp = [[minus_inf]*N for _ in range(2)]
dp[0][0] = arr[0]
for ind in range(1,N):
    dp[0][ind] = max(dp[0][ind-1]+arr[ind],arr[ind])
    dp[1][ind] = max(dp[0][ind-1],dp[1][ind-1]+arr[ind])

print(max(map(max,dp)))
