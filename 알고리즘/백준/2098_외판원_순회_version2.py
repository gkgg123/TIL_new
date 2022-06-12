def TSP(ind,visited_city):
    if dp[ind][visited_city] != -1:
        return dp[ind][visited_city]
    if visited_city == (1<<N)-1:
        if arr[ind][0]:
            return arr[ind][0]
        else:
            return INF
    dp[ind][visited_city] = INF
    for next_city in range(N):
        if ind == next_city:
            continue
        if visited_city & (1<<next_city):
            continue
        if arr[ind][next_city]:
            dp[ind][visited_city] = min(dp[ind][visited_city],TSP(next_city,visited_city|1<<next_city) + arr[ind][next_city])

    return dp[ind][visited_city]


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

INF = float('inf')
dp = [[-1]*(2**N) for _ in range(N)]
result = INF


print(TSP(0,1))
