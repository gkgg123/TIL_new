import sys

input = sys.stdin.readline

def union(A,B):
    X = find_parent(A)
    Y = find_parent(B)
    if X != Y:
        if rank[X] < rank[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if rank[X] == rank[Y]:
            rank[X] += 1

def find_parent(ind):
    if make_set[ind] == ind:
        return ind
    else:
        make_set[ind] = find_parent(make_set[ind])
        return make_set[ind]


N,M = map(int,input().split())

make_set = [i for i in range(N+1)]
rank =  [1 for _ in range(N+1)]
for _ in range(M):
    command, A,B = map(int,input().split())

    if command:
        if find_parent(A) == find_parent(B):
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
    else:
        union(A,B)