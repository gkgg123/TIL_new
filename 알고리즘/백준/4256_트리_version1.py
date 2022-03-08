import sys


def input():
    return sys.stdin.readline().rstrip()


def solve(root_idx,left,right):
    for idx in range(left,right):
        if inorder[idx] == preorder[root_idx]:
            solve(root_idx+1,left,idx)
            solve(root_idx + idx +1 - left, idx+1,right)
            print(preorder[root_idx], end=' ')
T = int(input())

for _ in range(T):
    N = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))

    solve(0,0,N)
    print()