import sys

def input():
    return sys.stdin.readline().rstrip()
def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)
    if X != Y:
        if ranks[X] < ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X

        if ranks[X] == ranks[Y]:
            ranks[X] += 1

def find_parents(x):
    if make_set[x] == x:
        return x
    make_set[x] = find_parents(make_set[x])
    return make_set[x]

N = int(input())
make_set = [i for i in range(N+1)]
ranks = [ 1 for _ in range(N+1)]
for _ in range(N-2):
    x,y = map(int,input().split())
    union(x,y)
    
for i in range(1,N+1):
    if i == find_parents(i):
        print(i,end=' ')