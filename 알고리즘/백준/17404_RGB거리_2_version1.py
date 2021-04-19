N = int(input())

INF = float('inf')



arr = [list(map(int,input().split())) for _ in range(N)]
result = float('inf')
for first_room in range(3):
    dp = [[INF]*3 for _ in range(N)]
    dp[0][first_room] = arr[0][first_room]
    for i in range(1,N-1):
        for k in range(3):
            for j in range(3):
                if k !=j:
                    dp[i][k] = min(dp[i-1][j]+arr[i][k],dp[i][k])

    for i in range(3):
        for j in range(3):
            if i != j and i != first_room:
                dp[N-1][i] = min(dp[N-2][j]+arr[N-1][i],dp[N-1][i])
    result = min(result,min(dp[N-1]))

print(result)