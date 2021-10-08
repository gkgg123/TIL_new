import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def dfs(*arg):
    queue = deque()
    queue.extend(arg)
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = -1
                    queue.append((nx,ny))
N,M = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
arr = [list(map(int,input().split())) for _ in range(N)]
arr[0][0] = -1
dfs((0,0))
time = 0
cheese = deque()
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            cheese.append((x,y))

if len(cheese) == 0:
    print(0)

while len(cheese)>0:
    melt_cheese = []
    for _ in range(len(cheese)):
        x,y = cheese.popleft()
        cnt = 0
        for i in range(4):
            nx =  x + dx[i]
            ny = y + dy[i]
            if arr[nx][ny] == -1:
                cnt += 1
        if cnt >=2:
            melt_cheese.append((x,y))
        else:
            cheese.append((x,y))

    for x,y in melt_cheese:
        arr[x][y] = -1
    if melt_cheese:
        dfs(*melt_cheese)
    time += 1

print(time)