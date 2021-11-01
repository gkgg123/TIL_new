import sys
from collections import defaultdict,deque
def input():
    return sys.stdin.readline()
def outOfBound(x,y):
    if 0<=x<N and 0<=y<M:
        return False
    return True
def check(position):
    for x,y in position:
        if arr[x][y] <K:
            return True
    return False
def blocking(a,b):
    if block_air[a].get(b):
        return True
    return False
def air_dire(dir):
    swap_dir = [[],[3,4],[3,4],[1,2],[1,2]]
    return [[0,dir],[swap_dir[dir][0],dir],[swap_dir[dir][1],dir]]
def calcurate(conditioner):
    air = [[0 for _ in range(M)] for _ in range(N)]
    for x,y in conditioner:
        dir = conditioner[(x,y)]
        x = x + dx[dir]
        y = y + dy[dir]
        air[x][y] += 5
        visited = set()
        visited.add((x,y))
        queue = deque()
        queue.append((x,y,5))

        while queue:
            x,y,cnt = queue.popleft()

            for total_dir in air_dire(dir):
                cx,cy = x,y
                for i in total_dir:
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if outOfBound(nx,ny):break
                    if blocking((cx,cy),(nx,ny)):break
                    cx,cy = nx,ny
                else:
                    if (cx,cy) not in visited:
                        visited.add((cx,cy))
                        air[cx][cy] = air[cx][cy] + cnt -1
                        if cnt >2:
                            queue.append((cx,cy,cnt-1))
    return air
def blow():
    temp = [[0 for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(M):

            for i in range(1,5):
                nx = x + dx[i]
                ny = y + dy[i]
                if outOfBound(nx,ny):continue
                if blocking((x,y),(nx,ny)):continue
                if arr[x][y] >= arr[nx][ny] + 4:
                    gap = (arr[x][y] - arr[nx][ny])//4
                    temp[x][y] -= gap
                    temp[nx][ny] += gap

    for x in range(N):
        for y in range(M):
            arr[x][y] += temp[x][y]
            if arr[x][y]<0:
                arr[x][y] = 0
def down():
    for x in range(N):
        for y in range(M):
            if x == 0 or y == 0 or y == M-1 or x == N-1:
                if arr[x][y]:
                    arr[x][y] -= 1
N,M,K = map(int,input().split())

arr = [[0 for _ in range(M)] for _ in range(N)]
# 1 동
# 2 서
# 3 북
# 4 남
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
air_conditioner = {}
check_position = []
for x in range(N):
    temp = list(map(int,input().split()))
    for y in range(M):
        if temp[y] and temp[y]<5:
            air_conditioner[(x,y)] = temp[y]
        elif temp[y] == 5:
            check_position.append((x,y))

W = int(input())
block_air = defaultdict(dict)
for _ in range(W):
    x,y,c = map(int,input().split())
    x -= 1
    y -= 1
    if c == 0:
        block_air[(x,y)][(x-1,y)] = 1
        block_air[(x-1,y)][(x,y)] = 1
    else:
        block_air[(x,y)][(x,y+1)] = 1
        block_air[(x,y+1)][(x,y)] = 1
temperature_arr = calcurate(air_conditioner)

time = 0
while check(check_position) and time<=100:
    
    for x in range(N):
        for y in range(M):
            arr[x][y] += temperature_arr[x][y]
    blow()
    down()
    time += 1
print(time)