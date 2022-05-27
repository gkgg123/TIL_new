import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def bfs():
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    time = 0
    while jihun:
        for _ in range(len(fire)):
            fx,fy = fire.popleft()
            for i in range(4):
                nx = fx + dx[i]
                ny = fy + dy[i]
                if 0<=nx<R and 0<=ny<C:
                    if miro[nx][ny] not in ('F','#'):
                        miro[nx][ny] = 'F'
                        fire.append((nx,ny))
        for _ in range(len(jihun)):
            cx,cy = jihun.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0<=nx<R and 0<=ny<C:
                    if miro[nx][ny] == '.':
                        miro[nx][ny] = 'J'
                        jihun.append((nx,ny))
                else:
                    return time+1
        time += 1
    return 'IMPOSSIBLE'



R,C = map(int,input().split())
INF = float('inf')
miro = []
jihun = deque()
fire = deque()
for x in range(R):
    temp = list(input())
    for y in range(C):
        if temp[y] == 'J':
            jihun.append((x,y))
        elif temp[y] == 'F':
            fire.append((x,y))
    miro.append(temp)

print(bfs())

