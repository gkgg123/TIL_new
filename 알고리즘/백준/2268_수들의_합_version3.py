import sys

input = sys.stdin.readline


def init(N):
    for i in range(N-1,0,-1):
        tree[i] = tree[i<<1] + tree[i<<1|1]

def query(left,right,N):
    ans = 0
    left = left +N
    right = right +N
    while left<right:
        if (left&1):
            ans += tree[left]
            left += 1
        if (right&1):
            right -= 1
            ans += tree[right]
        
        left >>= 1
        right>>= 1
    return ans


def update(pos,val,N):
    tree[pos+N] = val
    pos = pos +N
    while pos > 1:
        tree[pos>>1] = tree[pos] + tree[pos^1]
        pos >>= 1
N,M = map(int,input().split())


tree = [0]*(3*N)


for _ in range(M):
    command = list(map(int,input().split()))
    if command[0] == 1:
        update(command[1],command[2],N)
    else:
        if command[1] > command[2]:
            command[1],command[2] = command[2],command[1]

        sys.stdout.write(str(query(command[1],command[2]+1,N))+'\n')
