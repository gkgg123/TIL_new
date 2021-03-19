import sys
input = sys.stdin.readline

def union(A,B):
    x = find_parent(A)
    y = find_parent(B)
    if x > y:
        x,y = y,x
    make_set[y] = x
    for i in range(N+1):
        if make_set[i] != i:
            make_set[i] = find_parent(make_set[i])

def find_parent(ind):
    if make_set[ind] == ind:
        return ind
     
    return find_parent(make_set[ind])
N = int(input())
M = int(input())
edges = []
for i in range(N):
    graph_list = list(map(int,input().split()))
    for j in range(N):
        if graph_list[j] == 1:
            edges.append((i+1,j+1))

tour_list = list(map(int,input().split()))
make_set = [i for i in range(N+1)]

for edge in edges:
    node_a,node_b = edge
    if find_parent(node_a) != find_parent(node_b):
        union(node_a,node_b)

init_value = make_set[tour_list[0]]
result = 'YES'
for city in tour_list:
    if init_value != make_set[city]:
        result = 'NO'
        break
print(result)