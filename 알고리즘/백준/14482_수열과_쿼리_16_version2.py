import sys
def input():
    return sys.stdin.readline().rstrip()

def init(N):
    for i in range(N-1,0,-1):
        tree[i] = min(tree[i<<1], tree[i<<1|1])


def update(index,val):
    index = index + N
    tree[index] = (val,tree[index][1])
    while index>=1:
        tree[index>>1] = min(tree[index],tree[index^1])
        index >>=1


def query(left,right,N):
    min_val = INF
    left = left+N
    right = right+N
    while left<right:
        if (left&1):
            min_val = min(min_val,tree[left])
            left += 1
        if (right&1):
            right -= 1
            min_val = min(min_val,tree[right])
        left >>=1
        right >>=1
    return min_val[1]
N = int(input())
arr = list(map(int,input().split()))
INF = (float('inf'),float('inf'))
tree = [INF]*(2*N)
for i in range(N):
    tree[i+N] = (arr[i],i+1)
init(N)
M = int(input())
result = []
for _ in range(M):
    c,a,b = map(int,input().split())
    if c == 1:
        update(a-1,b)
    else:
        result.append(str(query(a-1,b,N)))


sys.stdout.write('\n'.join(result))