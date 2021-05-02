import sys

input = sys.stdin.readline


N = int(input())
tree = [[-1 for _ in range(2)] for _ in range(N+1)]
for i in range(1,N+1):
    left_ndoe,right_node = map(int,input().split())
    tree[i][0] = left_ndoe
    tree[i][1] = right_node



K = int(input())
cu_node = 1
while K >=0:
    left_or_right = K%2
    
    if tree[cu_node][0] != -1 and tree[cu_node][1] != -1:
        if left_or_right:
            cu_node = tree[cu_node][0]
        else:
            cu_node = tree[cu_node][1]
        K = K//2 + left_or_right
    else:
        if tree[cu_node][0] == -1 and tree[cu_node][1] == -1:
            break
        elif tree[cu_node][1] == -1:
            cu_node = tree[cu_node][0]
        else:
            cu_node = tree[cu_node][1]

print(cu_node)