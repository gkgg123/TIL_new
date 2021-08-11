import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()


def dfs(cur_idx,parent_idx):
    global cnt
    depth[cur_idx] = depth[parent_idx] + 1


    if tree[cur_idx][0] != -1:
        dfs(tree[cur_idx][0],cur_idx)
    cnt += 1
    width[depth[cur_idx]].append(cnt) 
    if tree[cur_idx][1] != -1:
        dfs(tree[cur_idx][1],cur_idx)

N = int(input())
root_check = [0 for _ in range(N+1)]
tree = [[-1 -1] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
width = defaultdict(list)
for _ in range(N):
    x,left_node,right_node = map(int,input().split())
    tree[x] = [left_node,right_node]
    if left_node != -1:
        root_check[left_node] += 1
    if right_node != -1:
        root_check[right_node] += 1
root_num = -1
for k in range(1,N+1):
    if root_check[k] == 0:
        root_num = k
        break


cnt = 0
dfs(root_num,0)

max_value = 0
max_depth = -1
for d in range(1,max(depth)+1):
    max_width,min_width = max(width[d]),min(width[d])
    if max_value < max_width - min_width + 1:
        max_value = max_width - min_width + 1
        max_depth = d

print(max_depth,max_value)
