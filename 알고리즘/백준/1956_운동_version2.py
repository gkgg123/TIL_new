import sys
from collections import defaultdict,deque
def input():
    return sys.stdin.readline().rstrip()

INF = float('inf')

V,E = map(int,input().split())

graph = defaultdict(list)

for _ in range(E):
    x,y,pay = map(int,input().split())
    graph[x].append((y,pay))

result = INF
queue = deque()
for start in graph:
    queue.append((start,start,0))

while queue:
    cur_node,end_position,cnt = queue.popleft()

    for next_node,val in graph[cur_node]:
        if val + cnt >= result:
            continue
        if end_position == next_node:
            result = min(result,cnt + val)
        else:
            queue.append((next_node,end_position, cnt + val))

print(-1 if result == INF else result)
