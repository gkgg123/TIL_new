import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())
mod = 2500
INF= float('inf')

arr = [list(input()) for _ in range(N)]
point_list = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

sx,sy = -1,-1
ex,ey = -1,-1


for x in range(N):
    for y in range(M):
        if arr[x][y] == 'g':
            point_list[x][y] = mod
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if arr[nx][ny] == '.':
                        point_list[nx][ny] = 1
        elif arr[x][y] == 'S':
            sx,sy = x,y
        elif arr[x][y] == 'F':
            ex,ey = x,y


node_list = []

heapq.heappush(node_list,(0,sx,sy))
distance_list = [[INF for _ in range(M)] for _ in range(N)]
distance_list[sx][sy] = 0
result = -1
while node_list:
    cp,x,y = heapq.heappop(node_list)

    if distance_list[x][y]<cp:
        continue

    if x == ex and y == ey:
        result = cp
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M:

            if distance_list[nx][ny] > cp + point_list[nx][ny]:
                distance_list[nx][ny] = cp + point_list[nx][ny]
                heapq.heappush(node_list,(distance_list[nx][ny],nx,ny))





print(result//mod,result%mod)