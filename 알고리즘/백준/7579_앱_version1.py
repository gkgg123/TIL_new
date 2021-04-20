N,M = map(int,input().split())
INF= float('inf')
dp = [INF]*(M+1)
apps_memory = list(map(int,input().split()))
apps_value = list(map(int,input().split()))
for i in range(N):
    memory,value = apps_memory[i],apps_value[i]
    for k in range(M,-1,-1):
        if k == 0:
            if memory >=M:
                memory = M
            dp[memory] = min(dp[memory],value)
        else:
            if dp[k]:
                num_memory = k + memory
                if num_memory >=M:
                    dp[M] = min(dp[M],dp[k]+value)
                else:
                    dp[num_memory] = min(dp[num_memory],dp[k]+value)
print(dp[M])