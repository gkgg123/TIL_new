import sys
def input():
    return sys.stdin.readline().rstrip()

def init(N):
    for i in range(N-1,0,-1):
        if arr[tree[i<<1]] <= arr[tree[i<<1|1]]:
            tree[i] = tree[i<<1]
        else:
            tree[i] = tree[i<<1|1]


def update(index):
    index = index + N
    while index>=1:
        if arr[tree[index]] < arr[tree[index^1]]:
            tree[index>>1] = tree[index]
        elif arr[tree[index]] == arr[tree[index^1]]:
            tree[index>>1] = min(tree[index],tree[index^1])
        else:
            tree[index>>1] = tree[index^1]
        index >>=1


def query(left,right,N):
    min_val = float('inf')
    min_idx = float('inf')
    left = left+N
    right = right+N
    while left<right:
        if (left&1):
            if min_val > arr[tree[left]]:
                min_val = arr[tree[left]]
                min_idx = tree[left]
            elif min_val == arr[tree[left]]:
                min_idx = min(min_idx,tree[left])
            left += 1
        if (right&1):
            right -= 1
            if min_val > arr[tree[right]]:
                min_val = arr[tree[right]]
                min_idx = tree[right]
            elif min_val == arr[tree[right]]:
                min_idx = min(min_idx,tree[right])
        left >>=1
        right >>=1
    return  min_idx
N = int(input())
arr = list(map(int,input().split()))
tree = [0]*(2*N)
for i in range(N):
    tree[i+N] = i
init(N)
M = int(input())
result = []
for _ in range(M):
    c,a,b = map(int,input().split())
    if c == 1:
        arr[a-1] = b
        update(a-1)
    else:
        result.append(str(query(a-1,b,N)+1))


sys.stdout.write('\n'.join(result))