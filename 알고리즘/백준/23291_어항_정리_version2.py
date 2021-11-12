import sys
def input():
    return sys.stdin.readline().rstrip()

def check(arr):
    if max(arr) - min(arr) <=K:
        return False
    return True
def push():
    min_value = min(arr)
    for i in range(N):
        if arr[i] == min_value:
            arr[i] += 1
def rotate(arr):
    row = len(arr)
    col = len(arr[0])
    rotate_arr = [[0 for _ in range(row)] for _ in range(col)]
    for x in range(row):
        for y in range(col):
            rotate_arr[y][row-x-1] = arr[x][y]
    return rotate_arr

def roll(arr):
    roll_arr = [[arr[0]],[arr[1]]]
    remain_arr = arr[2:]
    while True:
        row = len(roll_arr)
        if row > len(remain_arr):break
        roll_arr = rotate(roll_arr) + [remain_arr[:row]]
        remain_arr = remain_arr[row:]
    for i in range(len(roll_arr)-1):
        roll_arr[i].extend([-1]*len(remain_arr))
    roll_arr[-1].extend(remain_arr)
    return roll_arr
def outOfbound(x,y,row,col):
    if 0<=x<row and 0<=y<col:
        return False
    return True
def blow():
    row = len(new_arr)
    col = len(new_arr[0])
    diff = []
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
                    diff.append((x,y,nx,ny,gap))
    for x,y,nx,ny,gap in diff:
        new_arr[x][y] -= gap
        new_arr[nx][ny] += gap
def flatting(maze):
    temp_arr = []
    row = len(maze)
    col = len(maze[0])
    for y in range(col):
        for x in range(row-1,-1,-1):
            if maze[x][y]==-1:continue
            temp_arr.append(maze[x][y])
    return temp_arr

def rotate_180(maze):
    return [row[::-1] for row in maze[::-1]]
def spread():
    spread_arr = flatting(new_arr)
    temp = [spread_arr]
    for _ in range(2):
        col = len(temp[0])
        left_division = rotate_180([row[:col//2] for row in temp])
        right_division = [row[col//2:] for row in temp]
        temp = left_division + right_division
    return temp
                
    
N,K = map(int,input().split())

arr = list(map(int,input().split()))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
turn = 0
while check(arr):
    push()
    new_arr = roll(arr)
    blow()
    new_arr = spread()
    blow()
    arr = flatting(new_arr)
    turn += 1
print(turn)
