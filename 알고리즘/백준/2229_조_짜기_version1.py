import sys

def input():
    return sys.stdin.readline().rstrip()
N = int(input())
arr = [0]+ list(map(int,input().split()))

dp = [0 for _ in range(N+1)]
diff = [[-1 for _ in range(N+1)] for _ in range(N+1)]



for i in range(2,N+1):
    dp[i] = dp[i-1]
    min_val = arr[i]
    max_val = arr[i]
    for j in range(i-1,-1,-1):
        dp[i] = max(dp[i],dp[j] + max_val-min_val)
        min_val = min(min_val,arr[j])
        max_val = max(max_val,arr[j])
print(dp[N])