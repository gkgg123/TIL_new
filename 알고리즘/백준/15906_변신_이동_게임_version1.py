import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

N,t,r,c = map(int,input().split())
r -=1; c-= 1
INF= float('inf')
distance = [[[INF,INF] for _ in range(N)] for _ in range(N)]
arr = [list(input()) for _ in range(N)]
distance[0][0][0] = 0
node_list = []
heapq.heappush(node_list,(0,0,0,0))
dx = [-1,0,1,0]
dy = [0,-1,0,1]

while node_list:
    dis,flag,x,y = heapq.heappop(node_list)
    if distance[x][y][flag] < dis:
        continue
    if (x,y) == (r,c):
        break
    if flag:
        last_position = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0<=nx<N and 0<=ny<N:
                if arr[nx][ny] == '#':
                    last_position.append((nx,ny))
                    break
                nx += dx[i]
                ny += dy[i]
        if last_position:
            for nx,ny in last_position:
                if distance[nx][ny][flag] > dis + 1:
                    distance[nx][ny][flag] = dis + 1
                    heapq.heappush(node_list,(distance[nx][ny][flag],1,nx,ny))

    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if distance[nx][ny][0] > dis + 1:
                distance[nx][ny][0] = dis + 1
                heapq.heappush(node_list,(distance[nx][ny][0],0,nx,ny))
    if not flag:
        heapq.heappush(node_list,(dis+t,1,x,y))

print(min(distance[r][c]))
