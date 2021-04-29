N = int(input())

arr = [0]+[int(input()) for _ in range(N)]

dp = [0]*(N+1)

dp[1] = arr[1]

for ind in range(2,N+1):
    if ind == 2:
        dp[ind] = dp[ind-1] + arr[ind]
    else:
        dp[ind] = max(dp[ind-3]+arr[ind-1]+arr[ind],dp[ind-2]+arr[ind],dp[ind-1])

print(dp[N])