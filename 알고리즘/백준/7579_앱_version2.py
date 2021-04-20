N,M = map(int,input().split())
INF= float('inf')

apps_memory = list(map(int,input().split()))
apps_value = list(map(int,input().split()))
total_sum = sum(apps_value)

dp = [0]*(total_sum+1)
result = INF
for i in range(N):
    for j in range(total_sum,apps_value[i]-1,-1):
        if j - apps_value[i] >=0:
            dp[j] = max(dp[j],dp[j-apps_value[i]]+apps_memory[i])
        if dp[j] >= M:
            result = min(j,result)

print(result)



