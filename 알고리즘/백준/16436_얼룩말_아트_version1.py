import sys

def input():
    return sys.stdin.readline().rstrip()


def rotate(x,y):
    global M
    nx = x + y
    ny = x -y +M
    return [nx,ny]

def calcurate(px,py,r):
    up_x = px-r
    up_y = py
    down_x = px+r
    down_y = py
    ro_up_x,ro_up_y = rotate(up_x,up_y)
    ro_down_x,ro_down_y = rotate(down_x,down_y)
    return [ro_up_x, ro_up_y, ro_down_x, ro_down_y]


M,N,K = map(int,input().split())

square_arr =[[0 for _ in range(M+2)] for _ in range(N+2)]
diamond_arr = [[0 for _ in range(N+M+2)] for _ in range(N+M+2)]
offset = N
for _ in range(K):
    command,*arg = map(int,input().split())
    if command == 1:
        sy,sx,ey,ex = map(lambda x : x+1,arg)
        square_arr[sx][sy] += 1
        square_arr[sx][ey+1] -= 1
        square_arr[ex+1][sy] -= 1
        square_arr[ex+1][ey+1] += 1
    else:
        py,px,r = map(lambda x : x+1,arg)
        r -= 1
        sx,sy,ex,ey = calcurate(px,py,r)
        diamond_arr[sx][sy] += 1
        diamond_arr[sx][ey+1] -= 1
        diamond_arr[ex+1][sy] -= 1
        diamond_arr[ex+1][ey+1] += 1





for x in range(1,N+1):
    for y in range(1,M+1):
        square_arr[x][y] = square_arr[x][y] + square_arr[x-1][y] + square_arr[x][y-1] - square_arr[x-1][y-1]


for x in range(1,N+M+1):
    for y in range(1,N+M+1):
        diamond_arr[x][y] = diamond_arr[x][y] + diamond_arr[x-1][y] + diamond_arr[x][y-1] - diamond_arr[x-1][y-1]


arr = [['.' for _ in range(M)] for _ in range(N)]

for x in range(1,N+1):
    for y in range(1,M+1):
        if (square_arr[x][y] + diamond_arr[x+y][x-y+M])%2:
            arr[x-1][y-1] = '#'
for row in arr:
    sys.stdout.write(''.join(row)+'\n')