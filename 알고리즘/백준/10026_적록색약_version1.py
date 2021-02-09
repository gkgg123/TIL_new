from collections import deque

def bfs(x,y,color):
    global N
    stack = deque()
    stack.append((x,y))
    if color == 'B':
        chk = 2
    else:
        chk = 3
    visited[x][y] = chk
    while stack:
        x,y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and arr[nx][ny] == color:
                    visited[nx][ny] = chk
                    stack.append((nx,ny))
    
def new_bfs(x,y,chk):
    global N
    stack = deque()
    stack.append((x,y))
    visited[x][y] = 0
    while stack:
        x,y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx<N and 0<=ny<N:
                if visited[nx][ny] == chk:
                    visited[nx][ny] = 0
                    stack.append((nx,ny))

N = int(input())


arr = [list(input()) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*N for _ in range(N)]
cnt_a = 0
cnt_b = 0
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            bfs(x,y,arr[x][y])
            cnt_a += 1

for x in range(N):
    for y in range(N):
        if visited[x][y]:
            new_bfs(x,y,visited[x][y])
            cnt_b += 1

print(cnt_a,cnt_b)