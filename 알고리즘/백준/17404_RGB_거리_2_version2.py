N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]


INF = float('inf')
result = INF
for first_room_color in range(3):
    dp = [[0]*3 for _ in range(N)]
    for i in range(3):
        if i == first_room_color:
            dp[0][i] = arr[0][i]
        else:
            dp[0][i] = INF

    for ind in range(1,N):
        dp[ind][0] = arr[ind][0] + min(dp[ind-1][1],dp[ind-1][2])
        dp[ind][1] = arr[ind][1] + min(dp[ind-1][0],dp[ind-1][2])
        dp[ind][2] = arr[ind][2] + min(dp[ind-1][0],dp[ind-1][1])

    for last_room_color in range(3):
        if last_room_color != first_room_color:
            if result > dp[N-1][last_room_color]:
                result = dp[N-1][last_room_color]

print(result)