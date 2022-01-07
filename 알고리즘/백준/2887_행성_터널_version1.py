import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def get_Weight(x1,x2,y1,y2,z1,z2):
    return min(abs(x1-x2),abs(y1-y2),abs(z1-z2))

def sort_edge(stan):
    edges.sort(key = lambda x : x[stan])

    for key in range(N-1):
        x1,y1,z1,ind1 = edges[key]
        x2,y2,z2,ind2 = edges[key+1]
        E = abs(edges[key][stan] - edges[key+1][stan])
        graph[ind1].append((E,ind2))
        graph[ind2].append((E,ind1))

N = int(input())

edges = []
for ind in range(N):
    x,y,z = map(int,input().split())
    edges.append((x,y,z,ind))

graph = [[] for _ in range(N)]

sort_edge(0)
sort_edge(1)
sort_edge(2)
INF = float('inf')
visited = [True for _ in range(N)]
visited[0] = False
node_list = graph[0]
heapq.heapify(node_list)
result = 0
while node_list:
    cur_dis,node = heapq.heappop(node_list)
    if not visited[node]:
        continue
    result += cur_dis
    visited[node] = False
    for next_dis,next_node in graph[node]:
        if visited[next_node]:
            heapq.heappush(node_list,(next_dis,next_node))


print(result)