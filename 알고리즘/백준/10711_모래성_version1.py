import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())


arr = [list(input()) for _ in range(N)]

sand_deque = deque()

dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]
for x in range(N):
    for y in range(M):
        if not arr[x][y].isdigit():
            sand_deque.append((x,y))
        else:
            arr[x][y] = int(arr[x][y])



time = 0

while True:
    remove_sand = deque()

    while sand_deque:
        x,y = sand_deque.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<N and 0<=ny<M):continue
            if arr[nx][ny] != '.':
                arr[nx][ny] -= 1
                if arr[nx][ny] == 0:
                    remove_sand.append((nx,ny))
                    arr[nx][ny] = '.'
    if remove_sand:
        sand_deque.extend(remove_sand)
        time += 1
    else:
        break

print(time)