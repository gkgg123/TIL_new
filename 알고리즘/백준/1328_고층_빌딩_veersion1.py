import sys

def input():
    return sys.stdin.readline().rstrip()


N,L,R = map(int,input().split())
dp = [[[0 for _ in range(R+1)] for _ in range(L+1)] for _ in range(N+1)]
dp[1][1][1] = 1
mod = 1000000007
for num in range(2,N+1):
    for left in range(1,L+1):
        for right in range(1,R+1):
            dp[num][left][right] = (dp[num-1][left-1][right] + dp[num-1][left][right-1] + dp[num-1][left][right]*(num-2))%mod
print(dp[N][L][R])