T,N,D,K = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()
tea_cnt = [0]*N
for ind in range(N):
    left = ind
    right = N-1
    tea_time = arr[ind]
    while left <=right:
        mid = (left+right)//2

        if arr[mid] >= tea_time+D:
            right = mid -1
        else:
            left = mid + 1
    tea_cnt[ind] = left - ind

dp = [[0]*(K+1) for _ in range(N+1)]
for idx in range(N):
    for drink_coffee in range(1,K+1):
        dp[tea_cnt[idx]+idx][drink_coffee] = max(dp[tea_cnt[idx]+idx][drink_coffee], dp[idx][drink_coffee-1]+tea_cnt[idx])
        dp[idx+1][drink_coffee] = max(dp[idx+1][drink_coffee],dp[idx][drink_coffee])
for row in dp:
    print(row)
print(max(map(max,dp)))