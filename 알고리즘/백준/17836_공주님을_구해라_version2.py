import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    INF = float('inf')
    visited = [[INF for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((0,0))
    visited[0][0] = 0
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    gram = (-1,-1)
    while queue:
        cx,cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] != INF:
                    continue
                if maze[nx][ny] == 1:
                    continue
                if maze[nx][ny]:
                    gram = (nx,ny)
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx,ny))
                if (nx,ny) == (N-1,M-1):
                    if gram != (-1,-1):
                        gx,gy = gram
                        return min(visited[nx][ny], visited[gx][gy] + abs(N-1-gx) + abs(M-1-gy))
                    return visited[nx][ny]
    if gram != (-1,-1):
        gx,gy =gram
        return visited[gx][gy] + abs(N-1-gx) + abs(M-1-gy)
    return INF





N,M,T = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(N)]
answer = bfs()

print('Fail' if answer > T else answer)