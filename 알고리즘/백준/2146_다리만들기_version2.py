import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def island_bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    island_check[x][y] = island_cnt
    temp = [(x,y)]
    while queue:
        x,y = queue.popleft()
        bridge_queue.append((x,y,island_cnt,0))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and arr[nx][ny]:
                    visited[nx][ny] = True
                    island_check[nx][ny] = island_cnt
                    queue.append((nx,ny))
                    temp.append((nx,ny))
    island_list.append(temp)

def bfs():
    global result
    while bridge_queue:
        x,y,island_num,dis = bridge_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if island_check[nx][ny] == island_num:
                    continue
                if result <= visited[nx][ny]:
                    return
                if not distance_list[nx][ny]:
                    distance_list[nx][ny] = dis + 1
                    island_check[nx][ny] = island_num
                    bridge_queue.append((nx,ny,island_num,dis+1))
                else:
                    if result > distance_list[nx][ny] + distance_list[x][y]:
                        result = distance_list[nx][ny] + distance_list[x][y]

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
island_list = []
island_check = [[0 for _ in range(N)] for _ in range(N)]
island_cnt = 1
dx = [-1,0,1,0]
dy = [0,-1,0,1]
bridge_queue = deque()
for x in range(N):
    for y in range(N):
        if arr[x][y] and not visited[x][y]:
            island_bfs(x,y)
            island_cnt += 1

result = float('inf')

distance_list = [[0 for _ in range(N)] for _ in range(N)]

bfs()

                
print(result)
