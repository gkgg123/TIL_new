import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())

arr = []
aircon = deque()
visited = [[[True for _ in range(4)] for _ in range(M)] for _ in range(N)]
total_set = set()
for x in range(N):
    temp = list(map(int,input().split()))
    for y in range(M):
        if temp[y] == 9:
            aircon.append((x,y,[0,1,2,3]))
            temp[y] = 0
            total_set.add((x,y))
            for i in range(4):
                visited[x][y][i] = False

    arr.append(temp)


if aircon:
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    rotate_dict = {
        1 : [0,-1,2,-1],
        2 : [-1,1,-1,3],
        3 : [3,2,1,0],
        4 : [1,0,3,2]
    }
    # 북,서,남,동
    while aircon:
        x,y,dire = aircon.pop()
        for i in dire:
            nx = x + dx[i]
            ny = y + dy[i]
            while 0<=nx<N and 0<=ny<M and visited[nx][ny][i] and visited[nx][ny][(i+2)%4] and not arr[nx][ny]:
                visited[nx][ny][i] = False
                visited[nx][ny][(i+2)%4] = False
                total_set.add((nx,ny))
                nx = nx + dx[i]
                ny = ny + dy[i]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny]:
                if rotate_dict[arr[nx][ny]][i] != -1:
                    visited[nx][ny][i] = False
                    visited[nx][ny][(i+2)%4] = False
                    visited[nx][ny][rotate_dict[arr[nx][ny]][i]] = False
                    total_set.add((nx,ny))
                    aircon.append((nx,ny,[rotate_dict[arr[nx][ny]][i]]))
                else:
                    visited[nx][ny][i] = False
                    visited[nx][ny][(i+2)%4] = False
                    total_set.add((nx,ny))
    print(len(total_set))
else:
    print(0)
