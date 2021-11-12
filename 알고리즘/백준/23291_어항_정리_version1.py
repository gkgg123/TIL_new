import sys
def input():
    return sys.stdin.readline().rstrip()

def check(arr):
    if max(arr) - min(arr) <=K:
        return False
    return True
def push():
    min_value = min(arr[-1])
    for i in range(N):
        if arr[-1][i] == min_value:
            arr[-1][i] += 1
def roll(arr):
    row,col = 1,1
    new_N = N
    time = 0
    while True:
        new_temp = [[-1 for _ in range(new_N-col)] for _ in range(row+1)]

        for y in range(col,new_N):
            new_temp[-1][y-col] = arr[-1][y]

        for y in range(col):
            for x in range(len(arr)):
                new_temp[y][len(arr)-x-1] = arr[x][y]
        new_N = new_N-col
        if time%2:
            row += 1
            col += 1
        time += 1
        arr = [row[:] for row in new_temp]
        row_N = len(new_temp)
        if row_N*(col+1) >N:
            break
    return arr
def outOfbound(x,y,row,col):
    if 0<=x<row and 0<=y<col:
        return False
    return True
def blow():
    row = len(new_arr)
    col = len(new_arr[0])
    temp = [[0 for _ in range(col)] for _ in range(row)]
    for x in range(row):
        for y in range(col):
            if new_arr[x][y] == -1:continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if outOfbound(nx,ny,row,col):continue
                if new_arr[nx][ny] == -1:continue
                if new_arr[x][y] - new_arr[nx][ny] >=5:
                    gap = (new_arr[x][y] - new_arr[nx][ny])//5
                    temp[x][y] -= gap
                    temp[nx][ny] += gap
    for x in range(row):
        for y in range(col):
            new_arr[x][y] += temp[x][y]
def flatting(maze):
    temp_arr = [[]]
    row = len(maze)
    col = len(maze[0])
    for y in range(col):
        for x in range(row-1,-1,-1):
            if maze[x][y]==-1:continue
            temp_arr[-1].append(maze[x][y])
    return temp_arr
def spread():
    spread_arr = flatting(new_arr)
    temp = [[-1 for _ in range(N//4)] for _ in range(4)]

    for x in range(4):
        if x%2:
            start_x = N//4*x
            y = 0
            while y<N//4:
                temp[x][y] = spread_arr[-1][start_x+y]
                y += 1
        else:
            y = N//4-1
            if x == 2:
                start_x = 0
            else:
                start_x = N//4*2
            while y>=0:
                temp[x][y] = spread_arr[-1][start_x]
                start_x += 1
                y -= 1
    return temp
                
    
N,K = map(int,input().split())

arr = [list(map(int,input().split()))]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
turn = 0
while check(arr[-1]):
    push()
    new_arr = roll(arr)
    blow()
    new_arr = spread()
    blow()
    arr = flatting(new_arr)
    turn += 1
print(turn)
