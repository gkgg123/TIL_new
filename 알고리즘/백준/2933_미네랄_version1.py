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
    copy_cave = [row[:] for row in cave]
    for point in cluster_entry:
        if cave[point[0]][point[1]] == 'x':
            visited = set()
            stack = deque()
            stack.append(point)
            visited.add(point)
            while stack:
                x,y = stack.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<R and 0<=ny<C:
                        if cave[nx][ny] == 'x' and ((nx,ny)) not in visited:
                            visited.add((nx,ny))
                            stack.append((nx,ny))
            visited = list(visited)
            flag = True
            for point in visited:
                if point[0] == (R-1):
                    flag = False
                    break
            if flag:
                for point in visited:
                    cave[point[0]][point[1]] = '.'
                cluster_list.append(visited)
    if cluster_list:
        for cluster in cluster_list:
            origin_cluster = [row[:] for row in cluster]
            while True:
                move_point = []
                flag = False
                for point in cluster:
                    nx = point[0]+1
                    ny = point[1]
                    if 0<=nx<R and cave[nx][ny] == '.':
                        move_point.append((nx,ny))
                    else:
                        flag = True
                        break
                else:
                    cluster = [row[:] for row in move_point]
                if flag:
                    break

            for point in origin_cluster:
                copy_cave[point[0]][point[1]] = '.'
            for point in cluster:
                copy_cave[point[0]][point[1]] = 'x'
    return copy_cave



R,C = map(int,input().split())

cave = [list(input()) for _ in range(R)]

N = int(input())
arr = list(map(int,input().split()))
for i in range(N):
    if i%2:
        break_point = BreakMineral(arr[i],True)
        if break_point != [-1,-1]:
            cave = DownCluster(break_point,True)
    else:
        break_point = BreakMineral(arr[i],False)
        if break_point != [-1,-1]:
            cave = DownCluster(break_point,False)


for row in cave:
    print(''.join(row))