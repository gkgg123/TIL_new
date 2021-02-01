# 3197번 Fail

import sys
def find(number):
    if parents[number] == number:
        return number
    parents[number] = find(parents[number])
    return parents[number]

def merge(root,child):
    parents[child] = root

def water_merge():
    while water:
        cx,cy = water.pop(0)
        flag = True
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0<= nx <R and 0<= ny <C:
                if check_map[nx][ny] != -1 and check_map[nx][ny] != check_map[cx][cy]:
                    parentA = find(check_map[cx][cy])
                    parentB = find(check_map[nx][ny])
                    if parentA != parentB:
                        merge(parentA,parentB)
                        check_map[nx][ny] = parentA
                elif check_map[nx][ny] == -1 and flag:
                    melt_water.append((cx,cy))
                    flag = False


def water_melt():
    while melt_water:
        cx,cy = melt_water.pop(0)
        root = find(check_map[cx][cy])
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0<= nx <R and 0<= ny <C:
                if check_map[nx][ny] == -1:
                    water.append((nx,ny))
                    check_map[nx][ny] = root        

R,C = map(int,input().split())

arr = [list(sys.stdin.readline()) for _ in range(R)]
check_map = [[-1]*C for _ in range(R)]
parents = [-1]*(R*C)
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
swan = []
water = []
for x in range(R):
    for y in range(C):
        if arr[x][y] == '.' or arr[x][y] == 'L':
            water.append((x,y))
            parents[cnt] = cnt
            check_map[x][y] = cnt
            cnt += 1
            if arr[x][y] == 'L':
                swan.append((x,y))

swan1 = swan[0]
swan2 = swan[1]
time = 0
melt_water = []
while water:
    water_merge()
    if find(check_map[swan1[0]][swan1[1]]) == find(check_map[swan2[0]][swan2[1]]):
        result = time
        break
    water_melt()
    time += 1

            
print(result)