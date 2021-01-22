from itertools import combinations
from collections import deque
def bfs(active_virus,total_virus):
    global result,virus_list,N
    virus_cnt = 0
    deactive_virus = virus_list-active_virus
    stack = deque()
    spend_time = [row[:] for row in spend_time_stand]
    for x,y in active_virus:
        stack.append((x,y,0))
        spend_time[x][y] = 0
        virus_cnt += 1
    min_time = -1
    while stack:
        x,y,time = stack.popleft()
        if min_time > result:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if spend_time[nx][ny] == -1 and (nx,ny) not in wall_list:
                    if (nx,ny) not in deactive_virus:
                        spend_time[nx][ny] = time+1
                        stack.append((nx,ny,time+1))
                        min_time = spend_time[nx][ny]
                        virus_cnt += 1
                    else:
                        spend_time[nx][ny] = 0
                        stack.append((nx,ny,time+1))
                        

        
    if total_virus == virus_cnt:
        if result >min_time and min_time != -1:
            result = min_time


    



N,M = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,1,-1]
arr = [list(map(int,input().split())) for _ in range(N)]
virus_list = set()
wall_list = set()
total_virus = N*N
spend_time_stand = [[-1] *N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if arr[x][y] == 2:
            virus_list.add((x,y))
        elif arr[x][y] == 1:
            wall_list.add((x,y))
            total_virus -= 1

start_virus_list = combinations(virus_list,M)
result = float('inf')
if total_virus-len(virus_list)+M != M:
    for lists in start_virus_list:
        bfs(set(lists),total_virus-len(virus_list)+M)
else:
    result = 0

if result == float('inf'):
    print(-1)
else:
    print(result)