import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def outOfBound(x,y):
    if 0<x<=N and 0<y<=M:
        return True
    return False
def OutOfBounds(x,y):
    if outOfBound(x,y) and outOfBound(x+A-1,y+B-1) and outOfBound(x+A-1,y) and outOfBound(x,y+B-1):
        return False
    return True

def Chks(x,y):
    if arr[x+A-1][y+B-1] - arr[x-1][y+B-1] - arr[x+A-1][y-1] + arr[x-1][y-1]:
        return True
    return False
def dfs():
    queue = deque()

    queue.append((*S,0))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited = [[False for _ in range(M+1)] for _ in range(N+1)]
    visited[S[0]][S[1]] = True
    while queue:
        cx,cy,dis = queue.popleft()


        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if OutOfBounds(nx,ny):
                continue
            if visited[nx][ny]:
                continue

            if Chks(nx,ny):
                continue
            visited[nx][ny] = True
            queue.append((nx,ny,dis+1))
            if [nx,ny] == E:
                return dis + 1
    return -1
N,M,A,B,K = map(int,input().split())


result = -1



arr = [[0 for _ in range(M+1)] for _ in range(N+1)]
for _ in range(K):
    x,y =map(int,input().split())
    arr[x][y] = 1

for x in range(1,N+1):
    for y in range(1,M+1):
        arr[x][y] = arr[x][y] + arr[x-1][y] + arr[x][y-1] - arr[x-1][y-1]
S = list(map(int,input().split()))

E =  list(map(int,input().split()))

print(dfs())