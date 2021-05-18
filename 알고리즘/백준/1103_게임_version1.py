import sys

sys.setrecursionlimit(100000)


def dfs(x,y):
    if visited[x][y]:
        return INF
    elif dp[x][y] >0:
        return dp[x][y]
    else:
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]*int(arr[x][y])
            ny = y + dy[i]*int(arr[x][y])
            if 0<=nx<N and 0<=ny<M and arr[nx][ny].isdigit():
                dp[x][y] = max(dp[x][y],dfs(nx,ny) + 1)
                if dp[x][y] == INF:
                    return INF
        visited[x][y] = False
    return dp[x][y]

            





dx = [-1,1,0,0]
dy = [0,0,1,-1]
N,M = map(int,input().split())
INF = float('inf')
arr = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]



result = dfs(0,0)

if result == INF:
    print(-1)
else:
    print(result+1)
