import sys
def dfs(x,y,result,total):
    global N,M,max_value
    if visited[x][y]:
        return
    if len(total) == 4:
        if max_value < result:
            max_value = result
        return
    visited[x][y] = 1
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0 <= ny <M:
            if not visited[nx][ny]:
                dfs(nx,ny,result+arr[nx][ny],total+[(nx,ny)])
    if len(total) == 3:
        center_x,center_y = total[1]
        for i in range(4):
            nx = center_x + dx[i]
            ny = center_y + dy[i]
            if 0<= nx < N and 0 <=ny<M:
                if not visited[nx][ny]:
                    dfs(nx,ny,result+arr[nx][ny],total+[(nx,ny)])
    visited[x][y] = 0
    return



N,M = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]


arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
max_value = 0
for x in range(N):
    for y in range(M):
        dfs(x,y,arr[x][y],[(x,y)])
print(max_value)