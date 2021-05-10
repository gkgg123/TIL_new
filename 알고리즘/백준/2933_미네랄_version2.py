# R,C 행,열
# 같은 클러스터
# 창영 동굴 왼쪽, 상근 오른쪽
from collections import deque
def BreakMineral(height,flag):
    y_list = sorted(list(range(C)),reverse=flag)
    height = R - height
    for y in y_list:
        if cave[height][y] == 'x':
            cave[height][y] = '.'
            return [height,y]
    
    return [-1,-1]

def DownCluster(input_point,flag):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    x,y = input_point
    cluster_entry = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C:
            if cave[nx][ny] == 'x':
                cluster_entry.append((nx,ny))

    
    cluster_list = []
    for point in cluster_entry:
        if cave[point[0]][point[1]] == 'x':
            stack = [point]
            visited = set()
            visited.add(point)
            flag = True
            while stack:
                x,y = stack.pop(0)
                if x == (R-1):
                    flag = False
                    break
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<R and 0<=ny<C:
                        if cave[nx][ny] == 'x' and ((nx,ny)) not in visited:
                            visited.add((nx,ny))
                            stack.append((nx,ny))
            if flag:
                visited = list(visited)
                for point in visited:
                    cave[point[0]][point[1]] = '.'
                cluster_list.append(visited)

    for cluster in cluster_list:
        move = 1
        flag = True
        while flag:
            for x,y in cluster:
                if x+move+1<R and cave[x+move+1][y] == '.':
                    continue
                else:
                    flag = False
                    break
            else:
                move += 1
        for x,y in cluster:
            cave[x+move][y] = 'x'



R,C = map(int,input().split())

cave = [list(input()) for _ in range(R)]

N = int(input())
arr = list(map(int,input().split()))
for i in range(N):
    if i%2:
        break_point = BreakMineral(arr[i],True)
        if break_point != [-1,-1]:
            DownCluster(break_point,True)
    else:
        break_point = BreakMineral(arr[i],False)
        if break_point != [-1,-1]:
            DownCluster(break_point,False)


for row in cave:
    print(''.join(row))