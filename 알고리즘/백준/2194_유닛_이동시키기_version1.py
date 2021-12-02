import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def outOfBound(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
def OutOfBounds(x,y):
    if outOfBound(x,y) and outOfBound(x+A-1,y+B-1) and outOfBound(x+A-1,y) and outOfBound(x,y+B-1):
        return False
    return True

def Chks(x,y):
    for cx in range(x,x+A):
        for cy in range(y,y+B):
            if arr[cx][cy]:
                return False
    return True
    
N,M,A,B,K = map(int,input().split())


result = -1



arr = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    x,y = map(lambda k: k-1, map(int,input().split()))
    arr[x][y] = 1


S = list(map(lambda k: k-1, map(int,input().split())))

E = list(map(lambda k: k-1, map(int,input().split())))


queue = deque()

queue.append((*S,0))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[False for _ in range(M)] for _ in range(N)]
visited[S[0]][S[1]] = True
while queue:
    cx,cy,dis = queue.popleft()
    if [cx,cy] == E:
        result = dis
        break

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if OutOfBounds(nx,ny):
            continue
        if visited[nx][ny]:
            continue
        if not Chks(nx,ny):
            continue
        visited[nx][ny] = True
        queue.append((nx,ny,dis+1))
print(result)