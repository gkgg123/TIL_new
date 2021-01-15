def dfs(bomblist):
    global N,result
    while bomblist:
        x,y = bomblist.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx == 0 or nx == N-1) or (ny == 0 or ny ==N-1):
                if arr[nx][ny] == 0:
                    break
        else:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx == 0 or nx == N-1) or (ny == 0 or ny ==N-1):
                    arr[nx][ny] -= 1
            result += 1
    return

            



N = int(input())
dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]
arr = [list(input()) for _ in range(N)]
result = 0
if N >4:
    result += (N-4)**2
bomb = []
for x in range(N):
    for y in range(N):
        if x == 1 or x == N-2:
            if arr[x][y] == '#':
                bomb.append((x,y))
            else:
                arr[x][y] = int(arr[x][y])
        elif 1<x<N-2:
            if y == 1 or y == N-2:
                bomb.append((x,y))
            else:
                if arr[x][y] != '#':
                    arr[x][y] = int(arr[x][y])
        else:
            if arr[x][y] != '#':
                arr[x][y] = int(arr[x][y])
dfs(bomb)
print(result)