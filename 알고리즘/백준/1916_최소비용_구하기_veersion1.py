N = int(input())
M = int(input())
graph ={i:[] for i in range(N+1)}
for i in range(M):
    node_x,node_y,fee = map(int,input().split())
    graph[node_x].append((node_y,fee))

start,end = map(int,input().split())
INFS = float('inf')
min_fees = [INFS] *(N+1)
visted = [0]*(N+1)
min_fees[start] = 0
visted[start] = 1
result = 0
node = start
while node != end:
    visted[node] = 1
    for next_node,fee in graph[node]:
        min_fees[next_node] = min(min_fees[next_node],min_fees[node]+fee)

    next_min_fees = INFS
    next_min_nodes = -1
    for ind in range(N+1):
        if not visted[ind] and next_min_fees > min_fees[ind]:
            next_min_fees = min_fees[ind]
            next_min_nodes = ind
    node = next_min_nodes


print(min_fees[end])