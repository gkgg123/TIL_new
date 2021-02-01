from collections import deque
import sys
R,C = map(int,input().split())

lake = [list(sys.stdin.readline()) for _ in range(R)]
waters = deque()
swans = []
water_chk = [[True] *C for _ in range(R)]
swan_chk = [[True] *C for _ in range(R)]
for x in range(R):
    for y in range(C):
        if lake[x][y] != 'X':
            waters.append((x,y))
            water_chk[x][y] = False
            if lake[x][y] == 'L':
                swans.append((x,y))
                lake[x][y] = '.'
start_swan,end_swan = swans
swans = deque()
swans.append(start_swan)
swan_chk[start_swan[0]][start_swan[1]] = False
times = 0
new_water = deque()
new_swans = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while True:
    while waters:
        x,y = waters.popleft()
        lake[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < R and 0<= ny <C:
                if lake[nx][ny] == 'X' and water_chk[nx][ny]:
                    new_water.append((nx,ny))
                    water_chk[nx][ny] = False
    while swans:
        x,y = swans.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx <R and 0<=ny<C:
                if swan_chk[nx][ny]:
                    if lake[nx][ny] == '.':
                        swans.append((nx,ny))
                    elif lake[nx][ny] == 'X':
                        new_swans.append((nx,ny))
                    swan_chk[nx][ny] = False

    if not swan_chk[end_swan[0]][end_swan[1]]:
        answer = times
        break
    waters = new_water
    swans = new_swans
    new_swans = deque()
    new_water = deque()
    times += 1

print(answer)