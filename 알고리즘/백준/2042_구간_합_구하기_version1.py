import math
import sys
input = sys.stdin.readline
def init(node_number,start,end):
    global segement_tree,arr
    if start == end:
        segement_tree[node_number] = arr[start]
        return segement_tree[node_number]
    else:
       segement_tree[node_number] = init(node_number*2, start, (start+end)//2) + init(node_number*2+1, (start+end)//2+1, end)
       return segement_tree[node_number]

def update(node_number,start,end,index,diff):
    global segement_tree
    if (index < start) or (index > end):
        return
    segement_tree[node_number] = segement_tree[node_number] + diff
    if (start != end):
        update( node_number*2, start , (start+end)//2,index,diff)
        update(node_number*2+1, (start+end)//2+1,end,index,diff)

def sum_range(node_number,start,end,left,right):
    global segement_tree
    if (left > end) or (right<start):
        return 0
    if (left <= start) and (end<=right):
        return segement_tree[node_number]
    return sum_range(node_number*2,start,(start+end)//2,left,right) + sum_range(node_number*2+1,(start+end)//2+1,end,left,right)

N,M,K = map(int,input().split())
height = math.ceil(math.log2(N))
tree_size = 2**(height+1)-1
segement_tree = [0]*tree_size
arr = [int(input()) for _ in range(N)]

init(1,0,N-1)
cnt = M+K
while cnt:
    command,number1,number2 = map(int,input().split())
    if command == 1:
        diffrence = number2 - arr[number1-1]
        arr[number1 - 1] = number2
        update(1,0,N-1,number1-1,diffrence)
    else:
        print(sum_range(1,0,N-1,number1-1,number2-1))
    cnt -= 1