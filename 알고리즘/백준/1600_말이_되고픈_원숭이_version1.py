# # 1600 말이 되고픈 원숭이
from collections import deque
K = int(input())
W,H = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(H)]

stack = deque()
stack.append((0,0,0,K))

visited = [[[0 for z in range(K+1)] for y in range(W)] for _ in range(H)]
visited[0][0][K] = 1
horse_move = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
move = [(-1,0),(1,0),(0,-1),(0,1)]
result = -1
while stack:
    x,y,cnt,horse_cnt = stack.popleft()
    if x+1 == H and y+1 == W:
        result = cnt
        break
    for dx,dy in move:
        nx = x + dx
        ny = y + dy
        if 0<=nx<H and 0<=ny<W:
            if not arr[nx][ny]:
                if not visited[nx][ny][horse_cnt]:
                    stack.append((nx,ny,cnt+1,horse_cnt))
                    visited[nx][ny][horse_cnt] = 1
    if horse_cnt:
        for dx,dy in horse_move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<H and 0<=ny<W:
                if not arr[nx][ny]:
                    if not visited[nx][ny][horse_cnt-1]:
                        stack.append((nx,ny,cnt+1,horse_cnt-1))
                        visited[nx][ny][horse_cnt-1] = 1



print(result)