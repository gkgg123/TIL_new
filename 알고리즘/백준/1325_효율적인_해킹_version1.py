
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
    
max_v = 0
result = []
v = [-1 for _ in range(n+1)]
for num in range(1,n+1):
    vi = [True for _ in range(n+1)]
    vi[num] = False
    q = deque([num])
    cnt = 0
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if vi[next_node]:
                vi[next_node] = False
                cnt += 1
                q.append(next_node)
    v[num] = cnt

max_v = max(v)
for ind in range(1,n+1):
    if v[ind] == max_v:
        print(ind,end=' ')