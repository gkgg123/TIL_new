import sys
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(100001)
def solve(N):
    if N == 0:
        return 1
    if dp[N]:
        return dp[N]
    total = 0
    for x in [N-2,N-4,N-6]:
        if x >=0:
            total = ( solve(x) + total) %mod
    dp[N] = total
    return dp[N]

T = int(input())
mod =  1000000009
dp = [0 for _ in range(100001)]
dp[1] = 1
dp[2] = 2
dp[3] = 2
for _ in range(T):
    N = int(input())

    s = solve(N)
    print(s)