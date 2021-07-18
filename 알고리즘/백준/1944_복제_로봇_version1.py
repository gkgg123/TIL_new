import sys
import heapq
from collections import deque
def input():
    return sys.stdin.readline()

N,M = map(int,input().split())

arr = [list(input()) for _ in range(N)]

start = [0,0,0]
node_list = []
total_cnt = 0
for x in range(N):
    for y in range(N):
        if arr[x][y] == 'S':
            start = [0,x,y]
            arr[x][y] = '0'



heapq.heappush(node_list,start)
INF = float('inf')
visited = [[True for _ in range(N)] for _ in range(N)]
distance = [[INF for _ in range(N)] for _ in range(N)]
result = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
while node_list:
    cur_dis,x,y, = heapq.heappop(node_list)
    if not visited[x][y]:
        continue
    if cur_dis > distance[x][y]:
        continue
    result += cur_dis
    cnt += 1
    visited[x][y] = False

    temp_visited = [[True for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((x,y,0))
    temp_visited[x][y] = False
    while queue:
        qx,qy,dis = queue.popleft()

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if temp_visited[nx][ny] and arr[nx][ny] != '1':
                temp_visited[nx][ny] = False
                queue.append((nx,ny,dis+1))
                if arr[nx][ny] == 'K' and distance[nx][ny] > dis+1:
                    distance[nx][ny] = dis + 1
                    heapq.heappush(node_list,(dis+1,nx,ny))
if cnt<M+1:
    print(-1)
else:
    print(result)