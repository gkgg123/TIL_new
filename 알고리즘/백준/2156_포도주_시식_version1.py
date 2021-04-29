N = int(input())

arr = [int(input()) for _ in range(N)]

dp = [[0 for _ in range(3)] for _ in range(N)] 
if N>2:
    dp[0][1] = arr[0]
    dp[1][1] = arr[1]
    dp[1][2] = dp[0][1] + arr[1]



    for ind in range(2,N):
        
        dp[ind][0] = max(dp[ind-1][0],dp[ind][0],dp[ind-2][2],dp[ind-2][1],dp[ind-1][1])
        dp[ind][1] = max(dp[ind][1],dp[ind-1][0]+arr[ind],dp[ind-2][1]+arr[ind],dp[ind-2][2]+arr[ind],dp[ind-2][0]+arr[ind])
        dp[ind][2] = max(dp[ind][2],dp[ind-1][1]+arr[ind])
    print(max(list(map(max,dp))))
else:
    print(sum(arr))