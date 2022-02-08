import sys
sys.setrecursionlimit(100005)
def input():
    return sys.stdin.readline().rstrip()
def mit():
    return map(int,input().split())

def make_tree(cur_node,parent_node):

    sizes[cur_node] = 1

    for next_node in tree[cur_node]:
        if next_node != parent_node:
            sizes[cur_node] += make_tree(next_node,cur_node)
    return sizes[cur_node]

N,R,Q = mit()
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    x,y = mit()
    tree[x].append(y)
    tree[y].append(x)
sizes = [-1 for _ in range(N+1)]

make_tree(R,R)
result = []
for _ in range(Q):
    node = int(input())
    result.append(str(sizes[node]))

sys.stdout.write('\n'.join(result))