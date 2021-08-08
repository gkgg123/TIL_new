import sys

def input():
    return sys.stdin.readline().rstrip()

def nC3(n):
    return (n*(n-1)*(n-2))//6

N = int(input())

graph_node_cnt = [0 for _ in range(N+1)]
edge_list = []
for _ in range(N-1):
    x,y = map(int,input().split())
    graph_node_cnt[x] += 1
    graph_node_cnt[y] += 1
    edge_list.append((x,y))

g_cnt = 0
d_cnt = 0
for node in range(1,N+1):
    if graph_node_cnt[node] >=3:
        g_cnt += nC3(graph_node_cnt[node])

for x,y in edge_list:
    if graph_node_cnt[x]>=2 and graph_node_cnt[y]>=2:
        d_cnt += (graph_node_cnt[x]-1)*(graph_node_cnt[y]-1)


if d_cnt>3*g_cnt:
    print('D')
elif d_cnt < 3*g_cnt:
    print('G')
else:
    print('DUDUDUNGA')
