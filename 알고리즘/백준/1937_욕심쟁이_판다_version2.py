import sys

sys.stdin = open('판다2.txt','r')

def dfs(x,y):
    global call
    call += 1
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        dp[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if bamboo[nx][ny]>bamboo[x][y]:
                    distance = dfs(nx,ny) + 1
                    dp[x][y] = max(distance,dp[x][y])
        return dp[x][y]







N = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
bamboo = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]
call = 0
result = - 1
for x in range(N):
    for y in range(N):
        if dp[x][y] == -1:
            dfs(x,y)

print(max(map(max,dp)))
print(call)