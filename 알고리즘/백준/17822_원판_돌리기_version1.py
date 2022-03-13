import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()
sys.stdin = open("17822.txt",'r')
def rotate(number,direction,cnt):
    if direction == 0:
        direction = cnt*1
    else:
        direction = cnt*-1
    rotate_number = number
    while rotate_number <=N:
        index = rotate_number -1
        origin[index].rotate(direction)
        rotate_number += number

def remove():
    flag = False
    visited = [[True for _ in range(M)] for _ in range(N)]
    
    for x in range(N):
        for y in range(M):
            if visited[x][y] and origin[x][y] != 0:
                queue = deque()
                queue.append((x,y))
                clear_set = [(x,y)]
                visited[x][y] = False
                while queue:
                    cx,cy = queue.popleft()

                    for i in range(4):
                        nx = cx + dx[i]
                        ny = (cy + dy[i])%M
                        if 0<=nx<N and 0<=ny<M:
                            if visited[nx][ny] and origin[nx][ny] == origin[x][y]:
                                queue.append((nx,ny))
                                visited[nx][ny] = False
                                clear_set.append((nx,ny))
                if len(clear_set)>1:
                    for cx,cy in clear_set:
                        origin[cx][cy] = 0
                    flag = True
            else:
                visited[x][y] = False
    return flag

def update():
    total_sum = 0
    total_cnt = 0
    for x in range(N):
        for y in range(M):
            total_sum += origin[x][y]
            if origin[x][y]:
                total_cnt += 1
    if not total_cnt:
        return
    mean_value = total_sum/total_cnt
    for x in range(N):
        for y in range(M):
            if not origin[x][y]:
                continue
            if origin[x][y] > mean_value:
                origin[x][y] -= 1
            elif origin[x][y] < mean_value:
                origin[x][y] += 1

N,M,T = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,-1,0,1]
origin = [deque(map(int,input().split())) for _ in range(N)]
for _ in range(T):
    number,direction,cnt = map(int,input().split())
    rotate(number,direction,cnt)
    flag = remove()
    if not flag:
        update()


result = 0
for row in origin:
    result += sum(row)
print(result)