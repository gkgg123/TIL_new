import sys
def input():
    return sys.stdin.readline().rstrip()



N,M = map(int,input().split())
MA = [0]+list(map(int,input().split()))
WA = [0]+list(map(int,input().split()))
MA.sort()
WA.sort()

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]


for x in range(1,N+1):
    for y in range(1,M+1):
        if x == y:
            dp[x][y] = dp[x-1][y-1] + abs(MA[x]-WA[y])
        elif x>y:
            dp[x][y] = min(dp[x-1][y-1] + abs(MA[x]-WA[y]), dp[x-1][y])
        else:
            dp[x][y] = min(dp[x-1][y-1] + abs(MA[x]-WA[y]), dp[x][y-1])

print(dp[N][M])