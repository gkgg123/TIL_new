import sys
def input():
    return sys.stdin.readline().rstrip()

def solve(N):
    if N%4 == 0:
        return foursquare(N)
    elif N%2:
        return oddsquare(N)
    else:
        return othersquare(N)
def oddsquare(size):
    arr = [[0 for _ in range(size)] for _ in range(size)]
    cnt = 1
    x,y = 0,size//2
    arr[x][y] = cnt
    while cnt <size*size:
        nx,ny = (x-1)%size ,(y+1)%size
        if arr[nx][ny]:
            nx,ny = (x+1)%size,y
        arr[nx][ny] = cnt+1
        x,y = nx,ny
        cnt += 1
    return arr

def foursquare(size):
    arr = [[0 for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            new_x = x-x//4*4
            new_y = y - y//4*4
            if new_x == new_y or new_x+new_y == 3:
                arr[x][y] = x*size+y+1
            else:
                arr[x][y] = (size - x-1)*size + (size-y)
    return arr

def othersquare(size):
    base_odd_square = oddsquare(size//2)
    arr = [[0 for _ in range(size)] for _ in range(size)]
    position = [0,2,3,1]
    half = size//2
    for x in range(size):
        for y in range(size):
            po = position[x//half*2 + y//half]
            num = po*half*half
            nx = x - x//half*half
            ny = y - y//half*half
            arr[x][y] = base_odd_square[nx][ny] + num
    swap_side = half//2
    swap_aside = swap_side-1

    for y in range(swap_side):
        for x in range(half):
            arr[x][y],arr[x+half][y] = arr[x+half][y],arr[x][y]
    
    for y in range(size-1,size-swap_aside-1,-1):
        for x in range(half):
            arr[x][y],arr[x+half][y] = arr[x+half][y],arr[x][y]

    arr[half//2][half//2], arr[half//2+half][half//2] = arr[half//2+half][half//2],arr[half//2][half//2]
    arr[half//2][half//2-1],arr[half//2+half][half//2-1] = arr[half//2+half][half//2-1],arr[half//2][half//2-1]

    return arr
N = int(input())
result = solve(N)


for row in result:
    print(*row)