import sys
from collections import deque

input = sys.stdin.readline
def bfs():
    global INF,result
    stack = deque()
    stack.append((0,0,1,0))
    visited = [[[INF for z in range(2)] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    visited[0][0][1] = 1
    while stack:
        x,y,dis,wall_cnt = stack.popleft()
        if x== N-1 and y == M-1:
            if result > dis:
                result = dis
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx< N and 0<= ny < M:
                if visited[nx][ny][wall_cnt] > dis + 1 and wall_cnt <=1:
                    if arr[nx][ny] == '1' and not wall_cnt:
                        visited[nx][ny][wall_cnt] = dis + 1
                        stack.append((nx,ny,dis+1,wall_cnt+1))
                    elif arr[nx][ny] == '0':
                        visited[nx][ny][wall_cnt] = dis +1
                        stack.append((nx,ny,dis+1,wall_cnt))


N,M = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
arr = [list(input()) for _ in range(N)]
wall = []
INF = float('inf')


result = INF
bfs()
if result == INF:
    print(-1)
else:
    print(result)