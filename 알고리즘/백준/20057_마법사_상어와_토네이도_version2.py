import sys

def blowSand(x,y,dire):
    global N
    ret = 0
    init_sand = arr[x][y]
    for i in range(10):
        if i == 9:
            sand = arr[x][y]
        else:
            sand = int(init_sand * rate[i]/100)
            arr[x][y] -= sand
        move_x = x + blowx[dire][i]
        move_y = y + blowy[dire][i]

        if 0<=move_x<N and 0<=move_y<N:
            arr[move_x][move_y] += sand
        else:
            ret += sand
    arr[x][y] = 0
    return ret

dx = [0,1,0,-1]
dy = [-1,0,1,0]
rate = [1, 1, 7, 7, 10, 10, 2, 2, 5]

blowx = [[-1, 1, -1, 1, -1, 1, -2, 2, 0,0], #left
[-1, -1, 0, 0, 1, 1, 0, 0, 2,1],   #down
[-1, 1, -1, 1, -1, 1, -2, 2, 0,0], #right
[1, 1, 0, 0, -1, -1, 0, 0, -2,-1],]  #up

blowy = [[1, 1, 0, 0, -1, -1, 0, 0, -2,-1],  #left
[-1, 1, -1, 1, -1, 1, -2, 2, 0,0], #down
[-1, -1, 0, 0, 1, 1, 0, 0, 2,1],   #right
[-1, 1, -1, 1, -1, 1, -2, 2, 0,0]] #up
N = int(sys.stdin.readline())
arr =[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
x,y = N//2,N//2
i = 1
dire = 0
result = 0
while i<=N:
    j = 0
    while j <int(i):
        x = x + dx[dire%4]
        y = y + dy[dire%4]
        result += blowSand(x,y,dire%4)
        j += 1
    dire += 1
    i += 0.5
print(result)