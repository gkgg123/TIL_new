# 5014 스타트링크
# F층 건물 스타트링크 있는 위치 G 강호가있는 층은 S
# U,D
import collections
def bfs(start,end,up,down):
    global F
    visited[start] = 1
    deque = collections.deque()
    deque.append((start,0))
    dx = [up,-down]
    result = 'use the stairs'
    while deque:
        num,cnt = deque.popleft()
        if num == end:
            result = cnt
            break
        for i in range(2):
            nx = num + dx[i]
            if 0 <= nx <= F:
                if not visited[nx]:
                    visited[nx] = 1
                    deque.append((nx,cnt+1))
    return result


F,S,G,U,D = map(int,input().split())
visited = [0]*(F+1)
visited[0] = 1

print(bfs(S,G,U,D))