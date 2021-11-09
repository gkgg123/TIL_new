import sys
from itertools import product
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
shark_dx = [0,-1,0,1,0]
shark_dy = [0,0,-1,0,1]
smells = [[-float('inf') for _ in range(4)] for _ in range(4)]
def input():
    return sys.stdin.readline().rstrip()
def solve():
        
    N,S = map(int,input().split())
    aqua = make_aqua()

    for _ in range(N):
        x,y,d = map(int,input().split())
        aqua[x-1][y-1][d-1] += 1
    sharks = tuple(map(lambda x: x-1,map(int,input().split())))
    time = 0
    while time<S:
        copy_aqua = [[col[:] for col in row] for row in aqua]
        aqua = move_fish(aqua,time,sharks)
        sharks = sharks_move(sharks,time,aqua)
        for x in range(4):
            for y in range(4):
                for d in range(8):
                    aqua[x][y][d] += copy_aqua[x][y][d]
        time += 1

    result = 0

    for x in range(4):
        for y in range(4):
            for i in range(8):
                result += aqua[x][y][i]
    sys.stdout.write(str(result))
def make_aqua():
    return [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
def outOfBound(x,y):
    if 0<=x<4 and 0<=y<4:
        return False
    return True

def move_fish(arr,T,sharks):
    n_a = make_aqua()
    for x in range(4):
        for y in range(4):
            for d in range(8):
                if arr[x][y][d]:
                    c_d = d
                    for _ in range(8):
                        nx = x + dx[c_d]
                        ny = y + dy[c_d]
                        if outOfBound(nx,ny) or (nx,ny) == sharks or smells[nx][ny] >= T-2:
                            c_d = (c_d-1)%8
                        else:
                            n_a[nx][ny][c_d] += arr[x][y][d]
                            break
                    else:
                        n_a[x][y][d] += arr[x][y][d]
    return n_a



def sharks_move(sharks,T,aqua):
    x,y = sharks

    max_move = (-1,-1,-1)
    max_eat = -1
    for k in product([1,2,3,4],repeat = 3):
        x,y = sharks
        visited = set()
        cnt = 0
        for d in k:
            nx = x + shark_dx[d]
            ny = y + shark_dy[d]
            if outOfBound(nx,ny):
                break
            elif (nx,ny) not in visited:
                visited.add((nx,ny))
                for i in range(8):
                    cnt += aqua[nx][ny][i]
            x,y = nx,ny
        else:
            if max_eat < cnt:
                max_eat = cnt
                max_move = k[:]

    x,y = sharks 
    for d in max_move:
        nx = x + shark_dx[d]
        ny = y + shark_dy[d]
        for i in range(8):
            if aqua[nx][ny][i]:
                aqua[nx][ny][i] = 0
                smells[nx][ny] = T
        x,y = nx,ny
    return x,y




if __name__ == '__main__':
    solve()