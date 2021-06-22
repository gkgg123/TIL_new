import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):

    queue = deque()
    queue.append((x,y))
    visited[x][y] = False
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] and arr[nx][ny] >= T:
                    visited[nx][ny] = False
                    queue.append((nx,ny))


N,M = map(int,input().split())

arr = []

for x in range(N):
    input_list = list(map(int,input().split()))
    temp = []
    for k in range(M):
        temp.append(sum(input_list[3*k:3*(k+1)]))

    arr.append(temp)

T = int(input())

T = 3*T


visited = [[True for _ in range(M)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] >= T  and visited[x][y]:
            bfs(x,y)
            cnt += 1

print(cnt)