import sys

def input():
    return sys.stdin.readline().rstrip()

def init(N):
    for i in range(N-1,0,-1):
        min_tree[i] = min(min_tree[i<<1],min_tree[i<<1|1])
        max_tree[i] = max(max_tree[i<<1],max_tree[i<<1|1])

def query(left,right,N):
    min_ans = float('inf')
    max_ans = 0
    left = left+N
    right = right+N
    while left<right:
        if (left&1):
            min_ans = min(min_ans,min_tree[left])
            max_ans = max(max_ans,max_tree[left])
            left += 1
        if (right&1):
            right -= 1
            min_ans = min(min_ans,min_tree[right])
            max_ans = max(max_ans,max_tree[right])
        left >>=1
        right >>=1
        print(left,right,'--')
    return [min_ans,max_ans]


N,M = map(int,input().split())

min_tree = [0]*(3*N)
max_tree = [0]*(3*N)

for i in range(N):
    val = int(input())
    min_tree[i+N] = val
    max_tree[i+N] = val

init(N)
for _ in range(M):
    x,y = map(int,input().split())
    print(*query(x-1,y,N))