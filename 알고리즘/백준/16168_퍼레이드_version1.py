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
V,E = map(int,input().split())


make_set = [i for i in range(V+1)]
ranks = [1 for _ in range(V+1)]
edge_cnt = [0 for i in range(V+1)]
for _ in range(E):
    x,y = map(int,input().split())
    edge_cnt[x] += 1
    edge_cnt[y] += 1
    union(x,y)


p = find_parents(1)
not_flag = False
for node in range(2,V+1):
    if p != find_parents(node):
        not_flag = True
        break
if not_flag:
    print('NO')
else:
    cnt = 0
    for node in range(1,V+1):
        if edge_cnt[node]%2:
            cnt += 1
        if cnt>2:
            break
    if cnt == 2 or cnt == 0:
        print('YES')
    else:
        print('NO')