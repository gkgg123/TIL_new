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
    result = set()
    for node in arg:
        union(node,0)
    party_dict = [[] for _ in range(N+1)]
    for ind in range(M):
        cnt,*party_arr = map(int,input().split())
        for node in party_arr:
            party_dict[node].append(ind)
        for x in range(cnt-1):
            for y in range(x+1,cnt):
                a,b = party_arr[x],party_arr[y]
                if get_parent(a) != get_parent(b):
                    union(a,b)
    parent = get_parent(0)
    for num in range(1,N+1):
        if get_parent(num) != parent:
            result.update(party_dict[num])
    print(len(result))

else:
    print(M)