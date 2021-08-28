import sys

def input():
    return sys.stdin.readline().rstrip()
def union(a,b):
    A = find_parent(a)
    B = find_parent(b)
    if A != B:
        if rank[A] < rank[B]:
            A,B = B,A
        make_set[B] = A
        if rank[A] == rank[B]:
            rank[A] += 1
        return True
    return False

def find_parent(ind):
    if make_set[ind] == ind:
        return ind
    else:
        make_set[ind] = find_parent(make_set[ind])
        return make_set[ind]

def kruskal():
    value = 0
    for p,x,y, in weight_list:
        if union(x,y):
            value += 1^p
    return value


N,M = map(int,input().split())
weight_list = []
for _ in range(M+1):
    x,y,p = map(int,input().split())
    weight_list.append((p,x,y))
make_set = list(range(N+1))
rank = [1]*(N+1)
weight_list.sort()
a = kruskal()
weight_list.sort(reverse=True)
make_set = list(range(N+1))
rank = [1]*(N+1)
b = kruskal()
print(a**2-b**2)
