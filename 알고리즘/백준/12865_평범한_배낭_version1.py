# 12865 평범한 배낭



N,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

dp = [0]*(K+1)
for i in range(N):
    weight,value = arr[i]
    for k in range(K,-1,-1):
        if k + weight <= K:
            if k == 0:
                dp[k+weight] = max(dp[k+weight],dp[k]+value)
            else:
                if dp[k]:
                    dp[k+weight] = max(dp[k+weight],dp[k]+value)
print(max(dp))