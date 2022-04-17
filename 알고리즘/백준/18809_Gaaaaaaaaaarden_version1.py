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
            temp[y] = 1
    arr.append(temp)
answer = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for grean_area in combinations(areas,G):
    rest_area = areas - set(grean_area)
    for red_area in combinations(rest_area,R):
        copy_arr = [row[:] for row in arr]
        visited = [[-1 for _ in range(M)] for _ in range(N)]
        queue = deque()
        cur_flower = 0
        for x,y in grean_area:
            queue.append((x,y,0,2))
            visited[x][y] = 0
            copy_arr[x][y] = 2
        for x,y, in red_area:
            queue.append((x,y,0,3))
            visited[x][y] = 0
            copy_arr[x][y] = 3

        while queue:
            len_q = len(queue)
            new_queue = deque()
            flower_area = set()
            for _ in range(len_q):
                cx,cy,time,color = queue.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if not copy_arr[nx][ny]:
                            continue
                        if copy_arr[nx][ny] == 1 and visited[nx][ny] == -1:
                            visited[nx][ny] = time + 1
                            copy_arr[nx][ny] = color
                            new_queue.append((nx,ny,time+1,color))
                        elif copy_arr[nx][ny] == color:
                            continue
                        elif copy_arr[nx][ny] != 1 and visited[nx][ny] == time+1:
                            flower_area.add((nx,ny))
            if flower_area:
                cur_flower += len(flower_area)
                while new_queue:
                    cx,cy,time,color = new_queue.popleft()
                    if (cx,cy) not in flower_area:
                        queue.append((cx,cy,time,color))
            else:
                queue = new_queue
        answer = max(answer,cur_flower)

print(answer)

        
            
