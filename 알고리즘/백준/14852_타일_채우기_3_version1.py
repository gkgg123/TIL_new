import sys

def input():
    return sys.stdin.readline().rstrip()

mod = 1000000007
N = int(input())

dp = [0 for _ in range(N+4)]
prefix = [0 for _ in range(N+4)]
dp[1] = 2
dp[2] = 7
prefix[2] = 1
for i in range(3,N+1):
    prefix[i] = (prefix[i-1] + dp[i-3])%mod
    dp[i] = (2*dp[i-1] + 3*dp[i-2] + 2*prefix[i])%mod
print(dp[N])
