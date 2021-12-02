import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def chk(x,y,base,target):
    dx = x - base[0]
    dy = y - base[1]
    move_x = target[0] - dx
    move_y = target[1] - dy
    if 0<= move_x<N and 0<=move_y <M:
        if S[0]<= move_x <= S[0]+A-1 and S[1] <=move_y <= S[1] +B-1:
            return True
    return False 
    
N,M,A,B,K = map(int,input().split())


result = -1



arr = [[0 for _ in range(M)] for _ in range(N)]
jangs = [list(map(lambda k: k-1, map(int,input().split()))) for _ in range(K)]


S = list(map(lambda k: k-1, map(int,input().split())))

E = list(map(lambda k: k-1, map(int,input().split())))

for i in range(N):
    for j in range(M):
        if chk(i,j,S,E):
            arr[i][j] = 2

for i in range(N):
    for j in range(M):
        for jang in jangs:
            if chk(i,j,S,jang):
                arr[i][j] = 1

for i in range(N):
    for j in range(M):
        _dx = i - S[0]
        _dy = j - S[1]
        sx,ex,sy,ey = S[0] + _dx,S[0]+A-1+_dx , S[1]+_dy ,S[1]+_dy-1+B
        if sx<0 or ex<0 or sx>=N or ex>=M:
            arr[i][j] = 1
        if sy<0 or ey<0 or ey>=M or ey>=M:
            arr[i][j] = 1
queue = deque()

queue.append((*S,0))
visited = [[False for _ in range(M)] for _ in range(N)]
visited[S[0]][S[1]] = True
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while queue:
    cx,cy,dis = queue.popleft()

    if arr[cx][cy] == 2:
        result = dis
        break

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if visited[nx][ny]:
                continue
            if arr[nx][ny] == 1:
                continue
            visited[nx][ny] = True
            queue.append((nx,ny,dis+1))
print(result)