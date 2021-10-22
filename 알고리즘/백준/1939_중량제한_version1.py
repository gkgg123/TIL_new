import sys
def input():
    return sys.stdin.readline().rstrip()

def find_parents(ind):
    if ind == parents[ind]:
        return ind
    parents[ind] = find_parents(parents[ind])
    return parents[ind]

def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)
    if X == Y:
        return False
    else:
        if ranks[X] < ranks[Y]:
            X,Y = Y,X
        parents[Y] = X
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True

N,M = map(int,input().split())

parents = [ind for ind in range(N+1)]
ranks = [1 for _ in range(N+1)]


graph = [{} for _ in range(N+1)]
for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y] = max(graph[x].get(y,0),pay)

queue = []

for cur_node in range(1,N+1):
    if graph[cur_node]:
        for next_node in graph[cur_node]:
            queue.append((graph[cur_node][next_node],cur_node,next_node))
queue.sort()
start_node, end_node = map(int,input().split())

while queue:
    weight,x,y = queue.pop()

    union(x,y)

    if find_parents(start_node) == find_parents(end_node):
        print(weight)
        break