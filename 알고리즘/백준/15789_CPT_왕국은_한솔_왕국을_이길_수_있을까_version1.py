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
        ranks[X] += ranks[Y]
N,M = map(int,input().split())
make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    union(x,y)


C,H,K = map(int,input().split())

king_list = []
CP = find_parents(C)
HP = find_parents(H)
for i in range(1,N+1):
    if i == find_parents(i):
        if i != CP and i != HP:
            king_list.append(ranks[i])


king_list.sort(reverse=True)

answer = ranks[CP] +  sum(king_list[:K])

print(answer)