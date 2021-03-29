def solution(ind,diff):
    if diff > 250000:
        return -INF
    if ind == N:
        if diff == 0:
            return 0
        else:
            return -INF
    if dp[ind][diff] != -1:
        return dp[ind][diff]

    dp[ind][diff] = solution(ind+1,diff+arr[ind])
    dp[ind][diff] = max(dp[ind][diff],solution(ind+1,diff))
    if arr[ind] > diff:
        dp[ind][diff] = max(dp[ind][diff],diff + solution(ind+1,arr[ind]-diff))
    else:
        dp[ind][diff] = max(dp[ind][diff],arr[ind] + solution(ind+1,diff-arr[ind]))
    return dp[ind][diff]

N = int(input())
arr = list(map(int,input().split()))
arr = arr + [0]
INF = float('inf')
dp = [[-1] * 500001 for _ in range(N+1)]

result = solution(0,0)
if result == 0:
    print(-1)
else:
    print(result)