def solution(m, n, puddles):
    answer = 0
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    max_num =  1000000007
    for i in range(n):
        for j in range(m):
            if [j+1,i+1] not in puddles:
                if i-1>=0:
                    dp[i][j] = (dp[i][j] +dp[i-1][j])%max_num
                if j-1>=0:
                    dp[i][j] = (dp[i][j-1] + dp[i][j])%max_num
                
    answer = dp[n-1][m-1]
    return answer