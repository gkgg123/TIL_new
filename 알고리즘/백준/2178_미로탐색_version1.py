# 2178번
# 문제
# N*M 크기의 배열
# (1,1) => (N,M) 까지 가야한다.
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
N,M = map(int,input().split())

maze = [list(input()) for _ in range(N)]


visted = [[0]*M for _ in range(N)]


stack = deque()
stack.append((0,0))
visted[0][0] = 1
flag = False
while not flag:
    x,y = stack.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == N-1 and ny == M-1:
            flag = True
            visted[nx][ny] = visted[x][y] + 1
            break
        elif 0<=nx<N and 0<=ny<M:
            if not visted[nx][ny] and maze[nx][ny] == '1':
                visted[nx][ny] = visted[x][y] + 1
                stack.append((nx,ny))
print(visted[N-1][M-1])