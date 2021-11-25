import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
possible_point = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
p_num = 1
size_list = [0]
result = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] and not visited[x][y]:
            que = deque()
            que.append((x,y))
            cnt = 1
            visited[x][y] = p_num
            while que:
                cx,cy = que.popleft()

                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if visited[nx][ny]:continue
                        if not arr[nx][ny]:continue
                        visited[nx][ny] = p_num
                        cnt += 1
                        que.append((nx,ny))
            size_list.append(cnt)
            p_num += 1
            if cnt > result:
                result = cnt
        elif not arr[x][y]:
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if arr[nx][ny]:
                        possible_point.append((x,y))
                        break


for x,y in possible_point:
    num_set = set()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny]:
                num_set.add(visited[nx][ny])
    cnt = 1
    for num in num_set:
        cnt += size_list[num]

    if result < cnt:
        result = cnt

print(result)