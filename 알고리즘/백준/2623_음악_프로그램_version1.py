import sys
from collections import deque

input = sys.stdin.readline


N,M = map(int,input().split())
graph = [set() for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
for _ in range(M):
    pdN,*arr = list(map(int,input().split()))

    for i in range(pdN-1):
        x,y = arr[i],arr[i+1]
        if y not in graph[x]:
            graph[x].add(y)
            degree[y] += 1

stack = deque()
cnt = 0
result = []
flag = True

for i in range(1,N+1):
    if degree[i]==0:
        stack.append(i)
while cnt<N:
    if not stack:
        flag = False
        break
    node = stack.popleft()
    result.append(str(node))
    for next_node in graph[node]:
        degree[next_node] -= 1

        if degree[next_node] == 0:
            stack.append(next_node)
    cnt += 1

if flag:
    print('\n'.join(result))
else:
    print(0)