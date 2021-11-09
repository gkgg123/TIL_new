import sys
def input():
    return sys.stdin.readline().rstrip()

def make_aqua():
    return [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
def outOfBound(x,y):
    if 0<=x<4 and 0<=y<4:
        return False
    return True

def move_fish(arr,T):
    new_aqua = make_aqua()
    for x in range(4):
        for y in range(4):
            for d in range(8):
                if arr[x][y][d]:
                    copy_d = d
                    for _ in range(8):
                        nx = x + dx[copy_d]
                        ny = y + dy[copy_d]
                        if outOfBound(nx,ny) or (nx,ny) == (shark_x,shark_y) or smells[nx][ny] >= T-2:
                            copy_d = (copy_d-1)%8
                        else:
                            new_aqua[nx][ny][copy_d] += arr[x][y][d]
                            break
                    else:
                        new_aqua[x][y][d] += arr[x][y][d]
    return new_aqua

def shark_swim(x,y,move,kill,visited):
    if len(move) == 3:
        return (kill,move)
    else:
        temp = (0,'000')
        for i in range(1,5):
            nx = x + shark_dx[i]
            ny = y + shark_dy[i]
            if outOfBound(nx,ny):continue
            if (nx,ny) not in visited:
                new_kill = sum(aqua[nx][ny])
                visited.add((nx,ny))
                temp = max(temp,shark_swim(nx,ny,move+str(i),kill + new_kill,visited))
                visited.remove((nx,ny))
            else:
                temp = max(temp,shark_swim(nx,ny,move+str(i),kill,visited))
        return temp

def sharks_move(sharks,T):
    x,y = sharks
    _,max_move = shark_swim(x,y,'',0,set())
    for d in max_move:
        d = int(d)
        nx = x + shark_dx[d]
        ny = y + shark_dy[d]
        for i in range(8):
            if aqua[nx][ny][i]:
                aqua[nx][ny][i] = 0
                smells[nx][ny] = T
        x,y = nx,ny
    return x,y



N,S = map(int,input().split())
aqua = make_aqua()

for _ in range(N):
    x,y,d = map(int,input().split())
    aqua[x-1][y-1][d-1] += 1

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
shark_dx = [0,0,1,0,-1]
shark_dy = [0,1,0,-1,0]
smells = [[-float('inf') for _ in range(4)] for _ in range(4)]
shark_x,shark_y = list(map(lambda x: x-1,map(int,input().split())))
time = 0
while time<S:
    copy_aqua = [[col[:] for col in row] for row in aqua]
    aqua = move_fish(aqua,time)
    shark_x,shark_y = sharks_move((shark_x,shark_y),time)
    for x in range(4):
        for y in range(4):
            for d in range(8):
                aqua[x][y][d] += copy_aqua[x][y][d]
    time += 1

result = 0

for x in range(4):
    for y in range(4):
        
        result += sum(aqua[x][y])
print(result)