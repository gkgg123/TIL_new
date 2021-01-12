def bfs(x,y,color):
    global puyo,visited,arr
    temp = [[x,y]]
    stack = [[x,y]]
    while stack:
        sx,sy = stack.pop(0)
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0<= nx < 12 and 0 <= ny <6:
                if arr[nx][ny] == color and visited[nx][ny]:
                    visited[nx][ny] = 0
                    stack.append([nx,ny])
                    temp.append([nx,ny])
    if len(temp) >= 4:
        return temp
    else:
        return []




arr = [list(input()) for _ in range(12)]
times = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while True:
    visited= [[1]*6 for _ in range(12)]
    puyo = []
    for x in range(12):
        for y in range(6):
            if arr[x][y] != '.' and visited[x][y]:
                visited[x][y] = 0
                check = bfs(x,y,arr[x][y])
                if check:
                    for x,y in check:
                        puyo.append((x,y))
    for x,y in puyo:
        arr[x][y] = '.'
    if len(puyo) == 0:
        break
    new_arr = [['.']*6 for _ in range(12)]
    for y in range(6):
        temp = []
        for x in range(11,-1,-1):
            if arr[x][y] != '.':
                temp.append(arr[x][y])
        for i in range(len(temp)):
            new_arr[11-i][y] = temp[i]
    arr = [row[:] for row in new_arr]
    times += 1
print(times)