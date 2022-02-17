import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()
def dfs(x,y,prev):
    cur_milk = (prev+1)%3
    if dp[x][y][cur_milk] != -1:
        return dp[x][y][cur_milk]
    total_eat = 0

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if arr[nx][ny] == cur_milk:
                total_eat = max(total_eat,dfs(nx,ny,arr[nx][ny]) +1)
            total_eat = max(total_eat,dfs(nx,ny,prev))
    dp[x][y][cur_milk] = total_eat
    return total_eat
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[[-1,-1,-1] for _ in range(N)] for _ in range(N)]
dx = [1,0]
dy = [0,1]
if arr[0][0]:
    print(dfs(0,0,2))
else:
    print(dfs(0,0,0)+1)