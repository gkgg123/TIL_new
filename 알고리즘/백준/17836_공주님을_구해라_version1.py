import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    INF = float('inf')
    visited = [[[INF,INF] for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 0
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while queue:
        cx,cy,_type = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny][_type] <= visited[cx][cy][_type] + 1:
                    continue
                if nx == N-1 and ny == M-1:
                    return visited[cx][cy][_type]+1
                if _type:
                    visited[nx][ny][_type] = visited[cx][cy][_type] + 1
                    queue.append((nx,ny,_type))
                elif maze[nx][ny] != 1:
                    if maze[nx][ny]:
                        queue.append((nx,ny,1))
                        visited[nx][ny][1] = visited[cx][cy][_type] + 1
                    else:
                        queue.append((nx,ny,0))
                    visited[nx][ny][_type] = visited[cx][cy][_type] + 1
    return INF
N,M,T = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(N)]
answer = bfs()

print('Fail' if answer > T else answer)
