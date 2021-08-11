import sys
sys.setrecursionlimit(1000000)
def input():
    return sys.stdin.readline().rstrip()
def inorder(node,flag ):
    k = 0
    if tree[node][0] != -1:
        k += inorder(tree[node][0],flag|True) + 2
    if tree[node][1] != -1:
        k += inorder(tree[node][1],flag|False) +( 2 if flag else 1)
    return k
N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N):
    root,a,b = map(int,input().split())
    tree[root].extend([a,b])
visited_set = set()
print(inorder(1,False))