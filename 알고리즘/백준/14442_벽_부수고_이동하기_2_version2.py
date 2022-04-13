import queue
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    queue = deque()
    queue.append((0,0,1))
    INF = float('inf')
    visited = [[INF for _ in range(M)] for _ in range(N)]
    visited[0][0] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y,dis = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if nx == N-1 and ny == M-1:
                    return dis+1
                if visited[nx][ny] > visited[x][y] + arr[nx][ny] and visited[x][y] + arr[nx][ny] <=K:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    queue.append((nx,ny,dis+1))
    return -1
N,M,K = map(int,input().split())

arr = [list(map(int,list(input()))) for _ in range(N)]


print(bfs())