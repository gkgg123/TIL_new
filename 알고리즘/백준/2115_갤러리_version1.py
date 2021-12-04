import sys


def input():
    return sys.stdin.readline().rstrip()
def outOfBound(x,y):
    if 0<=x<N and 0<=y<M:
        return False
    return True
def pick(x,y):
    global res
    for idx in range(4):
        flag = True
        for emp in range(1,2):
            nx = x + check[idx][emp][0]
            ny = y + check[idx][emp][1]
            if outOfBound(nx,ny) or arr[nx][ny] == 'X':
                flag = False
                break
        if not flag:
            continue
        for wall in range(2):
            nx = x + check[idx][wall][0] + dx[idx]
            ny = y + check[idx][wall][1] + dy[idx]
            if outOfBound(nx,ny) or arr[nx][ny] != 'X':
                flag = False
                break
            if not gallay[nx][ny][idx]:
                flag = False
                break
        if flag:
            for wall in range(2):
                nx = x + check[idx][wall][0] + dx[idx]
                ny = y + check[idx][wall][1] + dy[idx]
                gallay[nx][ny][idx] = False
            res += 1

            


N,M = map(int,input().split())


arr = [list(input()) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

check = [[[0,0],[0,1]], 
[[0,0],[1,0]],
[[0,0],[0,1]],
[[0,0],[1,0]]]

gallay = [[[True for _ in range(4)] for _ in range(M)] for _ in range(N)]


res = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] == '.':
            pick(x,y)

print(res)