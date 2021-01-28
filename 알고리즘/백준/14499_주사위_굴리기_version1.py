# 14499 주사위 굴리기
# N*M 지도
# 주사위는 윗면이 1 동쪽방향이 3인 상태로 놓아진다.
def roll(direction,nx,ny):
    global dice,map_list
    if direction == 1:
        dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
    elif direction == 2:
        dice[0],dice[2],dice[3],dice[5] = dice[2],dice[5],dice[0],dice[3]
    elif direction == 3:
        dice[0],dice[1],dice[4],dice[5] = dice[4],dice[0],dice[5],dice[1]
    else:
        dice[0],dice[1],dice[4],dice[5] = dice[1],dice[5],dice[0],dice[4]
    if map_list[nx][ny]:
        dice[5] = map_list[nx][ny]
        map_list[nx][ny] = 0
    else:
        map_list[nx][ny] = dice[5]


N,M,X,Y,K = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(N)]

# [1,2,3,4,5,6] 
# 동쪽 1 [4,2,1,6,5,3]
# 서쪽 2 [3,2,6,1,5,4]
# 북쪽 3 [5,1,3,4,6,2]
# 남쪽 4 [2,6,3,4,1,5]
dice = [0]*6
dire = [(0,1),(0,-1),(-1,0),(1,0)]

command_list = list(map(int,input().split()))
for command in command_list:
    nx = X + dire[command-1][0]
    ny = Y + dire[command-1][1]
    if 0<=nx<N and 0<=ny<M:
        roll(command,nx,ny)
    else:
        continue
    X,Y = nx,ny
    print(dice[0])