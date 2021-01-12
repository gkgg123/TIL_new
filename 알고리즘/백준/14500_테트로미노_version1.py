
def dfs(x,y,value,cnt):
    global N,M,max_value
    if cnt == 4:
        if max_value < value:
            max_value = value
        return 
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx <N and 0<= ny <M:
                if visted[nx][ny] == 0:
                    visted[nx][ny] = 1
                    dfs(nx,ny,value+arr[nx][ny],cnt+1)
                    visted[nx][ny] = 0


def check(x,y):
    global N,M,max_value
    another_matrix = [[[0,-1],[0,0],[0,1],[1,0]],
    [[0,-1],[0,0],[0,1],[-1,0]],
    [[-1,0],[1,0],[0,0],[0,1]],
    [[-1,0],[1,0],[0,0],[0,-1]]]
    for tus in another_matrix:
        flag = True
        temp = 0
        for cx,cy in tus:
            nx = x + cx
            ny = y + cy
            if 0<= nx <N and 0<= ny<M:
                temp += arr[nx][ny]
            else:
                flag = False
                break
        if flag:
            if max_value < temp:
                max_value = temp
N,M = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
arr = [list(map(int,input().split())) for _ in range(N)]
visted = [[0]*M for _ in range(N)]
max_value = 0
for x in range(N):
    for y in range(M):
        visted[x][y] = 1
        dfs(x,y,arr[x][y],1)
        visted[x][y] = 0
        check(x,y)


print(max_value)