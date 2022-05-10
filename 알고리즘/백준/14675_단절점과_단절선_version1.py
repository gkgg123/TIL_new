import sys

def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(100000)

def dfs(node,parent):
    global order_cnt
    order[node] = order_cnt
    lower[node] = order_cnt
    order_cnt += 1
    sub_tree = 0
    for next_node in graph[node]:
        if next_node == parent:
            continue
        if not order[next_node]:
            sub_tree += 1
            dfs(next_node,node)
            if sub_tree >1:
                answer.add(node)
            elif lower[next_node] >= order[node] and node != 1:
                answer.add(node)
        lower[node] = min(lower[node],lower[next_node])
            


N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


M = int(input())
order = [0 for _ in range(N+1)]
lower = [float('inf') for _ in range(N+1)]
order_cnt = 1
answer = set()
dfs(1,1)
for _ in range(M):
    t,order = map(int,input().split())
    if t == 2:
        print('yes')
    elif order in answer:
        print('yes')
    else:
        print('no')