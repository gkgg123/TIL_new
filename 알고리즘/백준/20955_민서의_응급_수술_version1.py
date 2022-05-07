import sys
def input():
    return sys.stdin.readline().rstrip()
def find_parents(x):
    if x == make_set[x]:
        return x
    make_set[x] = find_parents(make_set[x])
    return make_set[x]
def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)
    if X != Y:
        if ranks[X] < ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True
    return False
N,M = map(int,input().split())
make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]
answer = 0
for i in range(M):
    x,y = map(int,input().split())
    if not union(x,y):
        answer += 1



for i in range(1,N+1):
    if find_parents(i) == i:
        answer += 1

answer -= 1
print(answer)
