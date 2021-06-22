import sys
from collections import deque
input = sys.stdin.readline


def bfs(point,dis_list,flag):
    dis_list[point[0]][point[1]] = arr[point[0]][point[1]]
    dx = [-1,0]
    dy = [0,1]

    stack = deque()
    stack.append((point[0],point[1]))

    while stack:
        x,y = stack.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]*flag
            if 0<=nx<N and 0<=ny<M:
                if dis_list[nx][ny] < dis_list[x][y] + arr[nx][ny]:
                    dis_list[nx][ny] = dis_list[x][y] + arr[nx][ny]
                    stack.append((nx,ny))
        


N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
INF =float('inf')
start_distance = [[-INF for _ in range(M)] for _ in range(N)]
end_distance = [[-INF for _ in range(M)] for _ in range(N)]

start_point = (N-1,0)
end_point = (N-1,M-1)
bfs(start_point,start_distance,1)
bfs(end_point,end_distance,-1)

max_value = -INF

for i in range(N):
    for j in range(M):
        if start_distance[i][j] + end_distance[i][j] > max_value:
            max_value = start_distance[i][j] + end_distance[i][j]
print(max_value)