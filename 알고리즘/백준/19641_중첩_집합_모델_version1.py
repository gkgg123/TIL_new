import sys
sys.setrecursionlimit(100001)
def input():
    return sys.stdin.readline().rstrip()

def dfs(node):
    global order
    tree[node][0] = order

    for next_node in connect[node]:
        if not tree[next_node][0]:
            order += 1
            dfs(next_node)
    order += 1
    tree[node][1] = order

N = int(input())


connect = [[] for _ in range(N+1)]

for _ in range(N):
    input_val = list(map(int,input().split()))

    cur_node = input_val[0]

    for next_node in input_val[1:]:
        if next_node != -1:
            connect[cur_node].append(next_node)
    connect[cur_node].sort()


root_number = int(input())
tree = [[0,0] for _ in range(N+1)]
order = 1
dfs(root_number)


for node in range(1,N+1):
    print(node,tree[node][0],tree[node][1])