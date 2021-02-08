# 16946 벽 부수고 이동하기 4
def dfs(x,y,index):
    global index_dict,N,M

    stack = [(x,y)]
    cnt = 1
    arr[x][y] = index
    while stack:
        cx,cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not arr[nx][ny]:
                    stack.append((nx,ny))
                    arr[nx][ny] = index
                    cnt += 1
    index_dict[index] = cnt





N,M = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
arr = [list(map(int,list(input()))) for _ in range(N)]

index = -1
index_dict = {}


result = [['0']*M for _ in range(N)]
for x in range(N):
    for y in range(M):
        if not arr[x][y]:
            dfs(x,y,index)
            index -= 1
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            temp = set()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if arr[nx][ny] != 1:
                        temp.add(arr[nx][ny])

            move_wall = 1
            for index in temp:
                move_wall += index_dict[index]
            result[x][y] = str(move_wall%10)

for row in result:
    print(''.join(row))