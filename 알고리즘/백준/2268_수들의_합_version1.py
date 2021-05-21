import sys
import math
def init():
    global tree_size

    for i in range(tree_size-1,0,-1):
        segement_tree[i] = segement_tree[i*2] + segement_tree[i*2+1]


def update(index,diff):
    while index >= 1:
        segement_tree[index] += diff
        index//=2

def sum_range(node_number,start,end,left,right):
    if left > end or start > right:
        return 0
    if (left <= start) and (end <= right):
        return segement_tree[node_number]
    return sum_range(node_number*2,start,(start+end)//2,left,right) + sum_range(node_number*2+1,(start+end)//2+1,end,left,right)
input = sys.stdin.readline

N,M = map(int,input().split())

height = math.ceil(math.log2(N))
tree_size = 2**height
total_size = 2**(height+1)

segement_tree = [0]*total_size

for i in range(N):
    segement_tree[tree_size + i] = 0
init()
for i in range(M):
    command = list(map(int,input().split()))
    if command[0] == 1:
        diff = command[2] - segement_tree[tree_size + command[1] - 1]
        update(command[1]+tree_size-1,diff)
    else:
        if command[1] > command[2]:
            command[1],command[2] = command[2],command[1]
        print(sum_range(1,0,tree_size-1,command[1]-1,command[2]-1))