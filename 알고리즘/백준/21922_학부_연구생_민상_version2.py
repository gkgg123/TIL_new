import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
visited = [[True for _ in range(M)] for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
U,L,D,R = 0,1,2,3
ROTATE = [[],[U,-1,D,-1],
[-1,L,-1,R],
[R,D,L,U],
[L,U,R,D]]

arr = [list(map(int,input().split())) for _ in range(N)]
stack = deque()
for x in range(N):
    for y in range(M):
        if arr[x][y] == 9:
            stack.append((x,y,[0,1,2,3]))


while stack:
    x,y,dire = stack.popleft()

    for i in dire:
        visited[x][y] = False
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if not (0<=nx<N and 0<=ny<M) or arr[nx][ny] == 9:
                break
            if arr[nx][ny]:
                i = ROTATE[arr[nx][ny]][i]
                visited[nx][ny] = False
                if i == -1:
                    break
            elif not arr[nx][ny]:
                visited[nx][ny] = False

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt += 1
print(cnt)