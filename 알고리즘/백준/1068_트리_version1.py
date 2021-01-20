N = int(input())

arr = list(map(int,input().split()))
parent = {i:[] for i in range(N)}
child = {i:[] for i in range(N)}
root_node = -1
for ind in range(N):
    if arr[ind] == -1:
        root_node = ind
    else:
        parent[ind].append(arr[ind])
        child[arr[ind]].append(ind)
remove_node = int(input())
if root_node != remove_node:
    remove_nodes = set()
    stack = [remove_node]
    visited = [True] * N
    while stack:
        node = stack.pop(0)
        remove_nodes.add(node)
        for k in child[node]:
            if visited[k]:
                visited[k] = False
                stack.append(k)
        parent_node = parent[node][0]
        child[parent_node].remove(node)

    leef_nodes = set()

    for ind in range(N):
        if not len(child[ind]):
            leef_nodes.add(ind)
    print(len(leef_nodes-remove_nodes))
else:
    print(0)
