import math
import sys
input = sys.stdin.readline
def init(node_number,start,end):
    global segement_tree,arr
    if start == end:
        segement_tree[node_number] = arr[start]
        return segement_tree[node_number]
    else:
        mid = (start+end)//2
        segement_tree[node_number] = min(init(node_number*2, start, mid) , init(node_number*2+1, mid+1, end))
        return segement_tree[node_number]

def find_min_number(node_number,start,end,left,right):
    global segement_tree,INF
    if (left > end) or (right<start):
        return INF
    if (left <= start) and (end<=right):
        return segement_tree[node_number]
    mid = (start+end)//2
    return min(find_min_number(node_number*2,start,mid,left,right), find_min_number(node_number*2+1,mid+1,end,left,right))

N,M = map(int,input().split())
INF = float('inf')
segement_tree = [-1]*(N*4+20)
arr = [int(input()) for _ in range(N)]
init(1,0,N-1)

for _ in range(M):
    left,right = map(int,input().split())
    print(find_min_number(1,0,N-1,left-1,right-1))