#  17086 아기 상어
import collections
dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

def bfs(x,y):
    deque = collections.deque()
    deque.append((x,y,0))
    visited = [[True]*M for _ in range(N)]
    visited[x][y] = True
    while deque:
        x,y,cnt = deque.popleft()
        if arr[x][y]:
            return cnt
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<=ny <M:
                if visited[nx][ny]:
                    deque.append((nx,ny,cnt+1))
                    visited[nx][ny] = False


N,M = map(int,input().split())


arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
for x in range(N):
    for y in range(M):
        if not arr[x][y]:
            temp = bfs(x,y)
            result = max(temp,result)

print(result)