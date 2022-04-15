import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def bfs(st):
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[st[0]][st[1]] = 0
    queue = deque()
    queue.append(st)
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == -1 and arr[nx][ny] != '1':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                    if arr[nx][ny] > '2':
                        return f'TAK\n{visited[nx][ny]}'

    return 'NIE'



N,M = map(int,input().split())

arr = []
start = (0,0)
for x in range(N):
    temp = input()
    for y in range(M):
        if temp[y] =='2':
            start = (x,y)
    arr.append(temp)



print(bfs(start))

