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



N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
island_list = []
island_check = [[0 for _ in range(N)] for _ in range(N)]
island_cnt = 1
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for x in range(N):
    for y in range(N):
        if arr[x][y] and not visited[x][y]:
            island_bfs(x,y)
            island_cnt += 1

result = float('inf')


for island_num in range(len(island_list)):
    queue = deque(island_list[island_num])

    visited = [[0 for _ in range(N)] for _ in range(N)]
    dis = 1
    while queue:
        q_size = len(queue)
        flag = False
        for _ in range(q_size):
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if island_check[nx][ny] != island_num+1 and not visited[nx][ny]:
                        visited[nx][ny] = dis
                        queue.append((nx,ny))
                        if island_check[nx][ny]:
                            result = min(result,dis-1)
                            flag = True
                            break
            if flag:
                break
        if flag:
            break
        dis += 1

print(result)
