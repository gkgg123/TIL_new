import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()


def LCS(X,Y):
    if depth[X] != depth[Y]:
        if depth[X]>depth[Y]:
            X,Y = Y,X
        for i in range(MAX_NODE-1,-1,-1):
            if (depth[Y]-depth[X] >= (1<<i)):
                Y = parents[Y][i]
    if X == Y:
        return X
    if (Y != X):
        for i in range(MAX_NODE-1,-1,-1):
            if parents[X][i] != parents[Y][i]:
                X = parents[X][i]
                Y = parents[Y][i]
    return parents[X][0]
def tree_make(idx,cur_node,node_cnt,parent_idx):
    if idx == len(binary_list):
        return
    if binary_list[idx] == 0:
        node_cnt += 1
        cur_node = node_cnt
        binary_search[idx+1] = cur_node
        tree[cur_node].visited.append(idx+1)
        tree[cur_node].parent = parent_idx
        depth[cur_node] = depth[parent_idx] + 1
        parents[cur_node][0] = parent_idx
        if cur_node != 1:
            parent_node = tree[cur_node].parent
            if tree[parent_node].left == None:
                tree[parent_node].left = cur_node
            else:
                tree[parent_node].right = cur_node
        tree_make(idx+1,cur_node,node_cnt,cur_node)
    else:
        binary_search[idx+1] = cur_node
        tree[cur_node].visited.append(idx+1)
        cur_node = tree[cur_node].parent
        tree_make(idx+1,cur_node,node_cnt,cur_node)



class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.visited = []

N = int(input())
binary_list = list(map(int,list(input())))
i,j = map(int,input().split())
tree = [Node(i) for i in range(N+1)]
MAX_NODE = 15
binary_search = [0 for _ in range(len(binary_list)+1)]
depth = [0 for _ in range(N+1)]
parents = [[0 for _ in range(MAX_NODE)] for _ in range(N+1)]

tree_make(0,0,0,0)
for par_idx in range(1,MAX_NODE):
    for k in range(1,N+1):
        parents[k][par_idx] = parents[parents[k][par_idx-1]][par_idx-1]

X,Y = binary_search[i],binary_search[j]

result_node = LCS(X,Y)
print(*tree[result_node].visited)
