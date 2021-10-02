import sys
from collections import deque
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def topological_sort(zeros):
    queue = deque()
    queue.append(1)
    indegree_topo = indegree[:]
    stack_time = [0 for _ in range(N+1)]
    while queue:
        node = queue.popleft()
        time = times[node]
        if node in zeros:
            time = 0
        for next_node in graph[node]:
            stack_time[next_node] = max(stack_time[next_node], stack_time[node] + time)
            indegree_topo[next_node] -= 1
            if not indegree_topo[next_node]:
                queue.append(next_node)
    return [node, stack_time[node] + times[node] ]
            
N,M,K = map(int,input().split())
times = [0] +  list(map(int,input().split()))


graph = [[] for _ in range(N+1)]

indegree = [0 for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    indegree[y] += 1

end_node,result = topological_sort([])

pick_list = set(range(2,N+1))
pick_list.remove(end_node)


for times_zeros in combinations(pick_list,K):
    _,temp = topological_sort(times_zeros)
    result = min(result,temp)
print(result)