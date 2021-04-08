from collections import deque

def rotate(start,lens,arr):
    x,y = start
    rotated_arr = [[0]*lens for _ in range(lens)]

    for i in range(lens):
        for j in range(lens):
            rotated_arr[j][lens-i-1] = arr[x+i][y+j]

    for i in range(lens):
        for j in range(lens):
            arr[x+i][y+j] = rotated_arr[i][j]

def bfs(x,y):
    global max_block,col_size
    stack = deque()
    stack.append((x,y))
    cnt = 0
    visited[x][y] = False
    while stack:
        x,y = stack.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<col_size and 0<=ny<col_size:
                if arr[nx][ny] and visited[nx][ny]:
                    stack.append((nx,ny))
                    visited[nx][ny] = False
    if cnt > max_block:
        max_block = cnt




N,Q = map(int,input().split())


arr = [list(map(int,input().split())) for _ in range(2**N)]
col_size = 2**N
total_size = (col_size)**2

L = list(map(int,input().split()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for k in L:
    lengths = 2**k
    size = lengths**2
    start = (0,0)
    cnt = 0
    while cnt < total_size//size:
        rotate(start,lengths,arr)
        start = (start[0],start[1]+lengths)
        if start[1] >= col_size:
            start = (start[0]+lengths,0)
        cnt += 1
    melt_down = []
    for x in range(col_size):
        for y in range(col_size):
            temp = 0
            if arr[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<col_size and 0<=ny<col_size:
                        if arr[nx][ny]:
                            temp += 1
                if temp <3:
                    melt_down.append((x,y))
    if melt_down:
        for x,y in melt_down:
            arr[x][y] -= 1
    
print(sum(map(sum,arr)))
max_block = 0
visited = [[True]*col_size for _ in range(col_size)]
for x in range(col_size):
    for y in range(col_size):
        if arr[x][y] and visited[x][y]:
            bfs(x,y)
print(max_block)