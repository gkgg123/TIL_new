import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N,T = map(int,input().split())


graph_set = set()
for _ in range(N):
    x,y = map(int,input().split())
    graph_set.add((x,y))

visited = set()
queue = deque()
visited.add((0,0))
queue.append((0,0,0))
result = -1
while queue:
    x,y,dis = queue.popleft()
    if y == T:
        result = dis
        break

    for ny in [y-2,y-1,y,y+1,y+2]:
        for nx in [x-2,x-1,x,x+1,x+2]:
            if 0<=nx<=1000000 and 0<=ny<=T:
                if (nx,ny) in visited:
                    continue
                if (nx,ny) in graph_set:
                    visited.add((nx,ny))
                    queue.append((nx,ny,dis+1))

print(result)
