import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    queue = deque()
    queue.append(1)
    if 1 in gomgom:
        return 'Yes'
    while queue:
        node = queue.pop()
        if not graph[node]:
            return 'yes'
        for next_node in graph[node]:
            if next_node in gomgom:
                continue
            queue.append(next_node)


    return 'Yes'

N,M = map(int,input().split())


graph = [[] for _ in range(N+1)]

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)



P = int(input())
gomgom = set(map(int,input().split()))
print(bfs())