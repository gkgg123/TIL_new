import sys
from collections import deque


input = sys.stdin.readline


N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
INF = float('inf')
distance_front = [[INF]*M for _ in range(N)]
distance_back = [[INF]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
stack1 = deque()
stack2 = deque()
distance_front[0][0] = 1
distance_back[N-1][M-1] = 0

stack1.append((0,0))
stack2.append((N-1,M-1))

while stack1:
    x,y = stack1.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <N and 0<= ny <M:
            if distance_front[nx][ny] == INF:
                distance_front[nx][ny] = distance_front[x][y] +1
                if arr[nx][ny] == '0':
                    stack1.append((nx,ny))

while stack2:
    x,y = stack2.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <N and 0<=ny <M:
            if distance_back[nx][ny] == INF:
                distance_back[nx][ny] = distance_back[x][y] + 1
                if arr[nx][ny] == '0':
                    stack2.append((nx,ny))

result = distance_front[N-1][M-1]

for x in range(N):
    for y in range(M):
        if arr[x][y] == '1':
            result = min(result,distance_front[x][y]+distance_back[x][y])

if result != INF:
    print(result)
else:
    print(-1)