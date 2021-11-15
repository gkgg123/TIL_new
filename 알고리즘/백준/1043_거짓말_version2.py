import sys
def input():
    return sys.stdin.readline().rstrip()

def get_parent(x):
    if x == make_set[x]:
        return x
    make_set[x] = get_parent(make_set[x])
    return make_set[x]
def union(x,y):
    X = get_parent(x)
    Y = get_parent(y)
    if X != Y:
        if ranks[X] < ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if ranks[Y] == ranks[X]:
            ranks[X] += 1
        
    
N,M = map(int,input().split())

num,*arg = list(map(int,input().split()))
make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]
if num:
    result = 0
    for node in arg:
        union(node,0)
    party_list = [list(map(int,input().split()))[1:] for _ in range(M)]
    for party in party_list:
        last = party[-1]
        for ind in range(len(party)-1):
            union(party[ind],last)
    
    parent = get_parent(0)

    for party in party_list:
        if get_parent(party[-1]) != parent:
            result += 1
    print(result)



else:
    print(M)