import sys

def input():
    return sys.stdin.readline().rstrip()
N = int(input())
INF = float('inf')
dp = [[INF for _ in range(N+1)] for _ in range(N+1)]
dp[1][1] = 0
arr = [[-INF for _ in range(N+1)]]
for _ in range(N):
    temp = [INF] + list(map(int,input().split()))
    arr.append(temp)
for x in range(1,N+1):
    for y in range(1,N+1):
        dp[x][y] = min(dp[x][y], dp[x-1][y] + max(arr[x][y] - arr[x-1][y] + 1,0) ,dp[x][y-1] + max(arr[x][y] - arr[x][y-1] + 1,0))


print(dp[N][N])