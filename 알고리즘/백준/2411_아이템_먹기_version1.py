import sys

def input():
    return sys.stdin.readline().rstrip()

N,M,A,B = map(int,input().split())

dp = [[[0 for _ in range(A+1)] for _ in range(M+1)] for _ in range(N+1) ] 

arr = [[0 for _ in range(M+1)] for _ in range(N+1)]

for _ in range(A):
    x,y = map(int,input().split())
    arr[x][y] = 1
for _ in range(B):
    x,y, = map(int,input().split())
    arr[x][y] = -1

dx = [1,0]
dy = [0,1]

if arr[1][1] == 1:
    dp[1][1][1] = 1
else:
    dp[1][1][0] = 1

for x in range(1,N+1):
    for y in range(1,M+1):
        if (x,y) == (N,M):continue
        for k in range(A+1):
            if not dp[x][y][k]:continue
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 1<=nx<=N and 1<=ny<=M:
                    if arr[nx][ny] == -1:continue
                    if arr[nx][ny] == 1:
                        dp[nx][ny][k+1] += dp[x][y][k]
                    else:
                        dp[nx][ny][k] += dp[x][y][k]

print(dp[N][M][A])