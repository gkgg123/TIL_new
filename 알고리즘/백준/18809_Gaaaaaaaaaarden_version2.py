import sys
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N,M,G,R = map(int,input().split())

arr = []

areas = set()

for x in range(N):
    temp = list(map(int,input().split()))
    for y in range(M):
        if temp[y] == 2:
            areas.add((x,y))
    arr.append(temp)
answer = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for grean_area in combinations(areas,G):
    rest_area = areas - set(grean_area)
    for red_area in combinations(rest_area,R):
        r_queue = deque()
        g_queue = deque()
        cur_flower = 0
        visited = [[-1 for _ in range(M)] for _ in range(N)]
        for x,y, in red_area:
            r_queue.append((x,y))
            visited[x][y] = 0
        for x,y in grean_area:
            g_queue.append((x,y))
            visited[x][y] = 0
        cur_time = 1
        while r_queue and g_queue:
            for _ in range(len(r_queue)):
                cx,cy = r_queue.popleft()
                if visited[cx][cy] < 0:
                    continue
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if visited[nx][ny] == -1 and arr[nx][ny]:
                            visited[nx][ny] = cur_time
                            r_queue.append((nx,ny))

            for _ in range(len(g_queue)):
                cx,cy = g_queue.popleft()
                if visited[cx][cy] < 0:
                    continue

                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if visited[nx][ny] == -1 and arr[nx][ny]:
                            visited[nx][ny] = 0
                            g_queue.append((nx,ny))
                        elif visited[nx][ny] == cur_time:
                            visited[nx][ny] = -2
                            g_queue.append((nx,ny))
                            cur_flower += 1
            cur_time += 1
        answer = max(answer,cur_flower)

print(answer)