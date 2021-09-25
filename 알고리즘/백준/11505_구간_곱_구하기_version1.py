import sys
def input():
    return sys.stdin.readline().rstrip()


def init(N):
    for i in range(N-1,0,-1):
        tree[i] = (tree[i<<1] * tree[i<<1|1])%mod

def query(left,right,N):
    ans = 1
    left = left + N
    right = right + N
    while left<right:
        if (left&1):
            ans *= tree[left]%mod
            left += 1
        if (right&1):
            right -= 1
            ans *= tree[right]%mod
        left >>=1
        right >>=1
    return ans%mod


def update(pos,val,N):
    tree[pos+N] = val
    pos = pos + N
    while pos > 1:
        tree[pos>>1] = (tree[pos] * tree[pos^1])%mod
        pos >>= 1
N,M,K = map(int,input().split())

tree = [0]*(2*N)
mod = 1000000007
for i in range(N):
    val = int(input())
    tree[i+N] = val

init(N)
for _ in range(M+K):
    command,b,c = map(int,input().split())
    if command == 1:
        update(b-1,c,N)
    else:
        sys.stdout.write(str(query(b-1,c,N))+'\n')