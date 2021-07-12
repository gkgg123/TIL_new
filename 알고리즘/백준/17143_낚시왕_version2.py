import sys
def input():
    return sys.stdin.readline().rstrip()

def fishing(y):
    for x in range(R):
        if pos[x][y]:
            size = sharks[pos[x][y]][4]
            del sharks[pos[x][y]]
            pos[x][y] = 0
            return size
    return 0
R,C,M = map(int,input().split())

sharks = {}

pos = [[0 for _ in range(C)] for _ in range(R)]
for num in range(1,M+1):
    x,y,speed,dire,size = map(int,input().split())
    x -= 1
    y -= 1
    dire -= 1
    sharks[num] = (x,y,speed,dire,size)
    pos[x][y] = num


result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
reverse = [1,0,3,2]
for y in range(C):
    if len(sharks)==0:
        break
    result += fishing(y)
    next_pos = [[0 for _ in range(C)] for _ in range(R)]
    eaten = []
    for num in sharks:
        shark_x,shark_y,speed,dire,size = sharks[num]
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


        if next_pos[nx][ny] != 0:
            prev_shark_num = next_pos[nx][ny]
            if sharks[prev_shark_num][4] < size:
                next_pos[nx][ny] = num
                sharks[num] = (nx,ny,speed,dire,size)
                eaten.append(prev_shark_num)
            else:
                eaten.append(num)

        else:
            next_pos[nx][ny] = num
            sharks[num] =  (nx,ny,speed,dire,size)
    for num in eaten:
        del sharks[num]
    pos = [row[:] for row in next_pos]

print(result)
