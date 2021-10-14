import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs(x,y):
    global max_room_cnt
    visited[x][y] = 0
    queue = deque()
    queue.append((x,y))
    room_position = [(x,y)]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            if arr[x][y] & 1<<i:continue
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny] == -1:
                visited[nx][ny] = 0
                room_position.append((nx,ny))
                queue.append((nx,ny))

    max_room_cnt = max(max_room_cnt,len(room_position))

    for x,y in room_position:
        visited[x][y] = len(room_position)
        room_number_arr[x][y] = base_room_number

M,N = map(int,input().split())


arr = [list(map(int,input().split())) for _ in range(N)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]
visited = [[-1 for _ in range(M)] for _ in range(N)]
room_number_arr = [[-1 for _ in range(M)] for _ in range(N)]
base_room_number = 0
max_room_cnt = 0
for x in range(N):
    for y in range(M):
        if visited[x][y] == -1:
            bfs(x,y)
            base_room_number += 1


max_avaible_cnt = max_room_cnt
for x in range(N):
    for y in range(M):

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if room_number_arr[x][y] == room_number_arr[nx][ny]:continue
                max_avaible_cnt = max(max_avaible_cnt,visited[x][y] + visited[nx][ny])

print(base_room_number)
print(max_room_cnt)
print(max_avaible_cnt)