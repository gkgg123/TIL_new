import sys
import heapq
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())



INF = float('inf')
step_trash = [[INF for _ in range(M)] for _ in range(N)]
arround_trash = [[INF for _ in range(M)] for _ in range(N)]

arround_trash_can = [[0 for _ in range(M)] for _ in range(N)]


arr = []
start = []
flower = []
for x in range(N):
    temp = list(input())
    for y in range(M):
        if temp[y] == 'S':
            start = (x,y)
        elif temp[y] == 'F':
            flower = (x,y)
    
    arr.append(temp)
dx = [-1,1,0,0]
dy = [0,0,-1,1]


for x in range(N):
    for y in range(M):
        if arr[x][y] == 'g':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if arr[nx][ny] == '.':
                        arround_trash_can[nx][ny] = 1

node_list = []

heapq.heappush(node_list,(0,0,start[0],start[1]))

step_trash[start[0]][start[1]] = 0
arround_trash[start[0]][start[1]] = 0
visited = [[True for _ in range(M)] for _ in range(N)]

while node_list:
    s_t,p_t,x,y = heapq.heappop(node_list)

    if not visited[x][y]:
        continue
    visited[x][y] = False


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny] == 'g':
                if step_trash[nx][ny] > s_t + 1:
                    step_trash[nx][ny] = s_t + 1
                    arround_trash[nx][ny] = p_t + arround_trash_can[nx][ny]
                    heapq.heappush(node_list,(step_trash[nx][ny], arround_trash[nx][ny], nx, ny))
            else:
                if step_trash[nx][ny] > s_t:
                    step_trash[nx][ny] = s_t
                    arround_trash[nx][ny] = p_t + arround_trash_can[nx][ny]
                    heapq.heappush(node_list,(step_trash[nx][ny],arround_trash[nx][ny],nx,ny))
                elif step_trash[nx][ny] == s_t and arround_trash[nx][ny] > p_t + arround_trash_can[nx][ny]:
                    step_trash[nx][ny] = s_t
                    arround_trash[nx][ny] =  p_t + arround_trash_can[nx][ny]
                    heapq.heappush(node_list,(step_trash[nx][ny],arround_trash[nx][ny],nx,ny))






x,y = flower

print(step_trash[x][y] , arround_trash[x][y])