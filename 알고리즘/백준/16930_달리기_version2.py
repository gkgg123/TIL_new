from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()
def solve():
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((x1,y1))
    visited[x1][y1] = 0
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            for l in range(1,K+1):
                nx = x + dx[i]*l
                ny = y + dy[i]*l
                if not outofBound(nx,ny) or arr[nx][ny] == '#':
                    break
                if visited[nx][ny] != -1 and visited[nx][ny] <= visited[x][y]:
                    break
                if visited[nx][ny] != -1:
                    continue
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                if (nx,ny) == (x2,y2):
                    return visited[nx][ny]
    return -1
def outofBound(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False


N,M,K = map(int,input().split())

arr = [list(input()) for _ in range(N)]

x1,y1,x2,y2 = map(lambda x: x-1,map(int,input().split()))

print(solve())
