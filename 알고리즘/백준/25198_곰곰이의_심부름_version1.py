import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def comb(l):
    return (l*(l-1))//2
def bfs():
    queue = deque()
    queue.append(st)
    visited = [-1 for _ in range(N+1)]
    parent_node = [0 for _ in range(N+1)]
    visited[st] = 1

    while queue:
        node = queue.popleft()
        if md == node:
            break
        for next_node in tree[node]:
            if visited[next_node] == -1:
                parent_node[next_node] = node
                visited[next_node] = visited[node] + 1
                queue.append(next_node)
    
    from_st_to_mid = [md]
    node = md
    while parent_node[node] != 0:
        node = parent_node[node]
        from_st_to_mid.append(node)

    queue = deque()
    queue.append(md)
    visited = [-1 for _ in range(N+1)]
    parent_node = [0 for _ in range(N+1)]
    visited[md] = 1

    while queue:
        node = queue.popleft()
        if ed == node:
            break
        for next_node in tree[node]:
            if visited[next_node] == -1:
                parent_node[next_node] = node
                visited[next_node] = visited[node] + 1
                queue.append(next_node)
    from_mid_to_end = [ed]
    node = ed
    while parent_node[node] != 0:
        node = parent_node[node]
        from_mid_to_end.append(node)
    total_length = len(set(from_mid_to_end + from_st_to_mid))
    over_length = len(from_mid_to_end) + len(from_st_to_mid) - total_length
    return comb(total_length) + comb(over_length)

N = int(input())

st,md,ed = map(int,input().split())

tree = [[] for _ in range(N+1)]


for _ in range(N-1):
    x,y = map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)

print(bfs())