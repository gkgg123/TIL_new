import sys
from collections import deque
import time
def isconnent_swan(start,end,standard_time):
    global R,C
    visited = [[True] * C for _ in range(R)]
    stack = deque()
    stack.append((start[0],start[1]))
    visited[start[0]][start[1]] = False
    while stack:
        x,y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <R and 0<= ny <C:
                if melt_time[nx][ny] <= standard_time and visited[nx][ny]:
                    visited[nx][ny] = False
                    stack.append((nx,ny))
                    if nx == end[0] and ny == end[1]:
                        return True

    return False


def find_max_spend_time():
    global R,C
    while waters:
        x,y,time = waters.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < R and 0<= ny < C:
                if melt_time[nx][ny] == -1:
                    melt_time[nx][ny] = time + 1
                    waters.append((nx,ny,time+1))
    return time
R,C = map(int,input().split())
origins = [list(sys.stdin.readline()) for _ in range(R)]
melt_time = [[-1]*C for _ in range(R)]
waters = deque()
swans = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for x in range(R):
    for y in range(C):
        if origins[x][y] != 'X':
            waters.append((x,y,0))
            melt_time[x][y] = 0
            if origins[x][y] == 'L':
                swans.append((x,y))


max_time = find_max_spend_time()
min_time = 0
result = 0
while min_time <= max_time:
    mid_time = (min_time + max_time)//2
    if isconnent_swan(swans[0],swans[1],mid_time):
        answer = mid_time
        max_time = mid_time - 1
    else:
        min_time = mid_time + 1

print(answer)