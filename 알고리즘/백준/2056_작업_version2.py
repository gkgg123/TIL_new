import sys

def input():
    return sys.stdin.readline()

N = int(input())
dp = [0 for _ in range(N+1)]
for idx in range(1,N+1):
    time,cnt,*arr = list(map(int,input().split()))

    for prev_node in arr:
        dp[idx] = max(dp[idx],dp[prev_node])
    dp[idx] += time
print(max(dp))