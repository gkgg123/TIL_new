import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def check(mid,S,E):
    queue = deque()
    queue.append(S)
    visited = [False for _ in range(N+1)]
    visited[S] = True
    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if visited[next_node]:continue
            if graph[node][next_node] >= mid:
                queue.append(next_node)
                visited[next_node] = True
                if next_node == E:
                    return True
    return False

N,M = map(int,input().split())
graph = [{} for _ in range(N+1)]
left = 0
right = 0

for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y] = max(graph[x].get(y,0),pay)
    graph[y][x] = max(graph[y].get(x,0),pay)
    right = max(right,pay)

right += 1
start_node, end_node = map(int,input().split())
while left+1 < right:
    mid = (left+right)//2
    if check(mid,start_node,end_node):
        left = mid
    else:
        right = mid

print(left)