import sys
sys.setrecursionlimit(100005)
def input():
    return sys.stdin.readline().rstrip()

def dfs(idx,p):
    global w
    w[idx] += w[p]
    for child in childs[idx]:
        dfs(child,idx)

N,M = map(int,input().split())
parents = [0]+list(map(int,input().split()))
childs = [[] for _ in range(N+1)]

for idx in range(2,N+1):
    parent = parents[idx]
    childs[parent].append(idx)
w = [0 for _ in range(N+1)]

for _ in range(M):
    idx,val = map(int,input().split())
    w[idx] += val 


dfs(1,0)

print(*w[1:])