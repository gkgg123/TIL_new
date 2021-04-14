import copy
def find_position(pools,num):
    for x in range(4):
        for y in range(4):
            if pools[x][y][0] == num:
                return (x,y)
    return False
def move_fish(pools,shark_x,shark_y):
    for fish_num in range(1,17):
        position = find_position(pools,fish_num)
        if position:
            x,y = position
            fish_dire = pools[x][y][1]

            for _ in range(8):
                nx = x + dx[fish_dire]
                ny = y + dy[fish_dire]
                if 0<=nx<4 and 0<=ny<4:
                    if not (nx == shark_x and ny == shark_y):
                        pools[x][y][0],pools[nx][ny][0] = pools[nx][ny][0],pools[x][y][0]
                        pools[x][y][1],pools[nx][ny][1] = pools[nx][ny][1],fish_dire
                        break
                fish_dire = (fish_dire+1)%8


def eating(x,y,pools):
    temp = []
    shark_dire = pools[x][y][1]
    for _ in range(3):
        nx = x + dx[shark_dire]
        ny = y + dy[shark_dire]
        if 0<=nx<4 and 0<=ny<4 and pools[nx][ny][0]>0:
            temp.append((nx,ny))
        x,y = nx,ny
    return temp


def solution(pools,shark_x,shark_y,cnt):
    global answer
    pools2 = [[col[:] for col in row]      for row in pools]
    eat_fish_size = pools2[shark_x][shark_y][0]
    pools2[shark_x][shark_y][0] = -1
    move_fish(pools2,shark_x,shark_y)
    find_fish = eating(shark_x,shark_y,pools2)
    answer = max(answer,eat_fish_size+cnt)

    for x,y in find_fish:
        solution(pools2,x,y,cnt+eat_fish_size)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

pools = []
for x in range(4):
    arr = list(map(int,input().split()))
    temp = []
    for y in range(4):
        fish_number,dire = arr[2*y],arr[2*y+1]
        temp.append([fish_number,dire-1])
    pools.append(temp)
answer = 0

solution(pools,0,0,0)
print(answer)