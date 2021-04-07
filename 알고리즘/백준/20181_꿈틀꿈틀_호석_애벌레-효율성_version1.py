N,K = map(int,input().split())

arr = list(map(int,input().split()))
dp = [0]*(N+1)
result = 0


left = 0
right = 0
sum_temp = 0
while right <=N:
    if sum_temp >=K:
        while sum_temp >= K:
            dp[right] = max(dp[right],dp[left]+sum_temp-K)
            sum_temp -= arr[left]
            left += 1
    else:
        dp[right] = max(dp[right],dp[right-1])
        if right == N:
            break
        sum_temp += arr[right]
        right += 1
print(dp[N])

