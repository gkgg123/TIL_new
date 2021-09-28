import sys

def input():
    return sys.stdin.readline().rstrip()


M,N,K = map(int,input().split())

square_arr =[[0 for _ in range(M+3)] for _ in range(N+3)]
diamond_arr = [[0 for _ in range(M+3)] for _ in range(N+3)]


for _ in range(K):
    command,*arg = map(int,input().split())
    if command == 1:
        sy,sx,ey,ex = map(lambda x : x+1,arg)
        square_arr[sx][sy] ^= 1
        square_arr[sx][ey+1] ^= 1
        square_arr[ex+1][sy] ^= 1
        square_arr[ex+1][ey+1] ^= 1
    else:
        py,px,r = map(lambda x : x+1,arg)
        r -= 1
        diamond_arr[px-r][py] ^= 1
        diamond_arr[px+1][py-r-1] ^=1
        diamond_arr[px+1][py+r+1] ^= 1
        diamond_arr[px+r+2][py] ^=1

        diamond_arr[px-r+1][py] ^=1
        diamond_arr[px+1][py-r] ^=1
        diamond_arr[px+1][py+r] ^=1
        diamond_arr[px+r+1][py] ^=1



    
for x in range(1,N+1):
    for y in range(1,M+1):
        square_arr[x][y] ^= square_arr[x][y-1]
for x in range(1,N+1):
    for y in range(1,M+1):
        square_arr[x][y] ^= square_arr[x-1][y]
 
for x in range(1,N+1):
    for y in range(M+1):
        diamond_arr[x][y] ^= diamond_arr[x-1][y+1]

for x in range(1,N+1):
    for y in range(1,M+1):
        diamond_arr[x][y] ^= diamond_arr[x-1][y-1]

arr = [['.' for _ in range(M)] for _ in range(N)]

for x in range(1,N+1):
    for y in range(1,M+1):
        if (square_arr[x][y] ^ diamond_arr[x][y]):
            arr[x-1][y-1] = '#'
for row in arr:
    sys.stdout.write(''.join(row)+'\n')