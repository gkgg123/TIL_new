import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()


N, M = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]


sx,sy,ex,ey = map(lambda x : x-1 ,map(int,input().split()))

arr = [list(map(int,input().split())) for _ in range(N)]


INF = float('inf')
distance_list = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(3)]


distance_list[1][sx][sy] = 0

dire_list = [[0,1,2,3],[0,2],[1,3]]

node_list = []

heapq.heappush(node_list,(0,sx,sy,1))


while node_list:
    cu_pay, cx, cy, cu_time = heapq.heappop(node_list)
    if distance_list[cu_time][cx][cy] < cu_pay:
        continue
    nx_time = (cu_time+1)%3
    if cx == ex and cy == ey:
        break

    for i in dire_list[cu_time]:
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny] != -1:

                if distance_list[nx_time][nx][ny] > cu_pay +arr[nx][ny]:
                    distance_list[nx_time][nx][ny] = cu_pay + arr[nx][ny]

                    heapq.heappush(node_list,(cu_pay + arr[nx][ny],nx,ny,nx_time)) 

result = INF
for i in range(3):
    result = min(result,distance_list[i][ex][ey])

if result == INF:
    print(-1)
else:
    print(result)