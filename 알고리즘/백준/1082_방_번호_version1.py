import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
P = list(map(int,input().split()))
M = int(input())

result = 0

dp = [-1 for _ in range(M+1)]
for num in range(N-1,-1,-1):
    coin = P[num]

    for k in range(coin,M+1):
        dp[k] = max(dp[k-coin]*10+num,num,dp[k])



print(dp[M])