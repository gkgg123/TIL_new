import heapq
import sys
input = sys.stdin.readline
def find_parents(X):
    if make_set[X] ==X:
        return X
    else:
        make_set[X] = find_parents(make_set[X])
        return make_set[X]


def union(a,b):
    X = find_parents(a)
    Y = find_parents(b)
    if X == Y:
        return False
    if rank[X]< rank[Y]:
        X,Y = Y,X
    make_set[Y] = X
    if rank[X] == rank[Y]:
        rank[X] += 1
    return True


P,W = map(int,input().split())

c,v = map(int,input().split())

weight_list = [list(map(int,input().split())) for _ in range(W)]
make_set = [i for i in range(P)]
weight_list.sort(key=lambda x : x[2])
rank = [1 for _ in range(P)]
result = float('inf')
while find_parents(c) != find_parents(v):
    node_a,node_b,pay = weight_list.pop()
    if union(node_a,node_b):
        result = pay


print(result)