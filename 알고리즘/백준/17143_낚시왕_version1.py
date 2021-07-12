import sys
def input():
    return sys.stdin.readline().rstrip()

def fishing(y):
    for x in sorted(shark_dict[y].keys()):
        if shark_dict[y][x]:
            temp = shark_dict[y][x][2]
            del shark_dict[y][x]
            return temp
    return 0
R,C,M = map(int,input().split())

shark_dict = [{} for _ in range(C)]
for _ in range(M):
    x,y,speed,dire,size = map(int,input().split())
    x -= 1
    y -= 1
    dire -= 1
    shark_dict[y][x] = [dire,speed,size]

result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
reverse = [1,0,3,2]
for y in range(C):
    remain_cnt = 0
    move_shark_dict = [{} for _ in range(C)]
    result += fishing(y)

    for shark_y in range(C):
        for shark_x in shark_dict[shark_y]:
            dire, speed, size = shark_dict[shark_y][shark_x]
            nx = shark_x + dx[dire]*speed
            ny = shark_y + dy[dire]*speed
            if dire in [0,1]:
                while not(0<=nx<R):
                    if nx<0:
                        nx = -nx
                        dire = reverse[dire]
                    else:
                        nx = (R-1)-(nx-(R-1))
                        dire = reverse[dire]
            else:
                while not(0<=ny<C):
                    if ny<0:
                        ny = -ny
                        dire = reverse[dire]
                    else:
                        ny = (C-1)-(ny-(C-1))
                        dire = reverse[dire]

            if move_shark_dict[ny].get(nx):
                if move_shark_dict[ny][nx][2] < size:
                    move_shark_dict[ny][nx] = [dire, speed, size]
            else:
                move_shark_dict[ny][nx] = [dire,speed,size]
                remain_cnt += 1
    if remain_cnt:
        shark_dict = [{} for _ in range(C)]

        for y in range(C):
            for x in move_shark_dict[y]:
                shark_dict[y][x] = move_shark_dict[y][x]
    else:
        break

print(result)
