def TSP(ind,visited_city):
    if dp[ind][visited_city] != INF:
        return dp[ind][visited_city]
    if visited_city == (1<<N)-1:
        if arr[ind][0]:
            return arr[ind][0]
        else:
            return INF

    for next_city in range(N):
        if not (visited_city&1<<next_city) and arr[ind][next_city]:
            temp = TSP(next_city,visited_city|1<<next_city) + arr[ind][next_city]
            dp[ind][visited_city] = min(dp[ind][visited_city],temp)

    return dp[ind][visited_city]





N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

INF = float('inf')
dp = [[INF]*(2**N) for _ in range(N)]

print(TSP(0,1))