# R,C 비어있는곳 . 물이 차있는 * 비버의 굴 d 고슴도치S 돌은 X



R,C = map(int,input().split())

arr = [list(input()) for _ in range(R)]
gos = []
end = []
water = []
visited = [[1] * C for _ in range(R)]
for x in range(R):
    for y in range(C):
        if arr[x][y] != '.' and arr[x][y] != 'X':
            if arr[x][y] == 'S':
                gos.append((x,y,0))
                visited[x][y] = 0
            elif arr[x][y] == 'D':
                end.extend((x,y))
            else:
                water.append((x,y))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
flag = False
water_time = - 1
while gos:
    x,y,time = gos.pop(0)
    if x == end[0] and y == end[1]:
        result = time
        flag = True
        break
    if water_time < time:
        new_water = []
        for wx,wy in water:
            for i in range(4):
                wnx = wx + dx[i]
                wny = wy + dy[i]
                if 0<= wnx <R and 0<= wny <C:
                    if arr[wnx][wny] == '.':
                        new_water.append((wnx,wny))
                        arr[wnx][wny] = '*'
        water_time += 1
        water = [row[:] for row in new_water]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < R and 0<= ny < C and visited[nx][ny]:
            if arr[nx][ny] == '.' or arr[nx][ny] == 'D':
                visited[nx][ny] = 0
                if nx == end[0] and ny == end[1]:
                    flag = True
                    result = time + 1
                    break
                gos.append((nx,ny,time+1))
    if flag:
        break
if flag:
    print(result)
else:
    print('KAKTUS')
