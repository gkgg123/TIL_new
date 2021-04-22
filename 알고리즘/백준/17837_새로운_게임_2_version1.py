import sys

input = sys.stdin.readline

def move(target):
    x,y,dire = chess[target]

    nx = x + dx[dire]
    ny = y + dy[dire]

    if not(0<=nx<N) or not(0<=ny<N) or arr[nx][ny] == 2:
        dire = reverse_dire[dire]
        chess[target] = [x,y,dire]
        nx = x + dx[dire]
        ny = y + dy[dire]
        if not(0<=nx<N) or not(0<=ny<N) or arr[nx][ny] == 2:
            return 0

    slice_idx = 0
    for ind,horse in enumerate(chess_map[x][y]):
        if horse == target:
            slice_idx = ind
            break

    move_items = chess_map[x][y][slice_idx:]
    chess_map[x][y] = chess_map[x][y][:slice_idx]

    if arr[nx][ny]:
        move_items.reverse()

    chess_map[nx][ny].extend(move_items)

    for ind in move_items:
        chess[ind] = [nx,ny,chess[ind][2]]
    
    return len(chess_map[nx][ny]) 



N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

chess = [[] for _ in range(M)]
chess_map = [[[] for _ in range(N)] for _ in range(N)]

chess_input = [list(map(lambda x : x-1,map(int,input().split()))) for _ in range(M)]


dx = [0,0,-1,1]
dy = [1,-1,0,0]
reverse_dire = [1,0,3,2]


for ind,info in enumerate(chess_input):
    x,y,dire = info
    chess[ind] = [x,y,dire]
    chess_map[x][y].append(ind)


cnt = 0
break_flag = False
while cnt <= 1000:
    cnt += 1

    for k in range(M):
        stack_size = move(k)
        if stack_size >= 4:
            break_flag = True
            break
    if break_flag:
        break

print(-1 if cnt > 1000 else cnt)