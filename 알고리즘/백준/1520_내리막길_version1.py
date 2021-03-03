def dfs(x,y):
    global N,M
    if x == N-1 and y == M-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] < arr[x][y]:
                    dp[x][y] += dfs(nx,ny)
        return dp[x][y]



import sys

input = sys.stdin.readline

N,M = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
print(dfs(0,0))