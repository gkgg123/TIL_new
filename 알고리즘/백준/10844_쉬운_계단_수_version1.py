N = int(input())

dp = [[0]*10 for _ in range(N)]


temp = [-1,1]
for i in range(N):
    for j in range(10):
        if i == N-1:
            if j == 0:
                continue
        if i == 0:
            dp[0][j] = 1
        else:
            for k in temp:
                nx = j+k
                if 0<=nx<10:
                    dp[i][j] += dp[i-1][j+k]

            
print(sum(dp[N-1])%1000000000)