import sys

def input():
    return sys.stdin.readline().rstrip()
while True:
    N,M = map(int,input().split())
    if not N+M:
        break
    dp = [[0 for _ in range(M+1)]]

    for _ in range(N):
        temp = [0]+list(map(int,input().split()))
        dp.append(temp)
    result = 0
    
    for x in range(1,N+1):
        for y in range(1,M+1):
            dp[x][y] = min(dp[x-1][y],dp[x][y-1],dp[x-1][y-1]) + 1 if dp[x][y] else 0

            if result<dp[x][y]:
                result = dp[x][y]
    print(result)

