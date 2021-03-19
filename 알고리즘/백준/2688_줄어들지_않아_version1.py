T = int(input())
dp = [[0]*10 if i !=0 else [1]*10 for i in range(65)]
visited = [0]*64
visited[0] = 1
last_n = 0
for ind in range(T):
    n = int(input())
    if visited[n-1]:
        print(sum(dp[n-1]))
    else:
        for ind in range(last_n+1,n):
            for num in range(9,-1,-1):
                if num == 9:
                    dp[ind][num] = sum(dp[ind-1])
                else:
                    dp[ind][num] = dp[ind][num+1] - dp[ind-1][num+1]
        last_n = max(last_n,n-1)

        print(sum(dp[n-1]))
