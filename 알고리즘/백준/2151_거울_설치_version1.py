import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def outOfBound(x,y):
    if 0<=x<N and 0<=y<N:
        return False
    return True
def bfs():
    x,y = start_door
    queue = deque()
    for i in range(4):
        queue.append((x,y,i,0))
        visited[x][y][i] = True
    while queue:
        x,y,dire,mirror_cnt = queue.popleft()
        
        while True:
            nx = x + dx[dire]
            ny = y + dy[dire]
            if outOfBound(nx,ny) or arr[nx][ny] == '*':
                break
            if visited[nx][ny][dire]:break
            if (nx,ny) == end_door:
                return mirror_cnt
            if arr[nx][ny] == '!':
                queue.append((nx,ny,(dire+1)%4,mirror_cnt+1))
                queue.append((nx,ny,(dire-1)%4,mirror_cnt+1))
            
            visited[nx][ny][dire] = True
            x = nx
            y = ny
                



N = int(input())

visited = [[[False for _ in range(4)] for _ in range(N)] for _ in range(N)]
# (1,0) => ()
dx = [1,0,-1,0]
dy = [0,-1,0,1]
doors = []
arr = []
for x in range(N):
    temp = list(input())

    for y in range(N):
        if temp[y] == '#':
            doors.append((x,y))
    arr.append(temp)

start_door = doors[0]
end_door = doors[1]

print(bfs())
