import sys

def input():
    return sys.stdin.readline().rstrip()
def find_parents(X):
    if X == make_set[X]:
        return X
    make_set[X] = find_parents(make_set[X])
    return make_set[X]
def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)
    if X !=Y:
        if ranks[X] < ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True

def connect(r1,r2):
    if (r1['x1'] > r2['x1'] and r1['y1'] > r2['y1']   and r1['x2'] < r2['x2']  and r1['y2'] < r2['y2']):
        return False
    if (r1['x1'] < r2['x1'] and r1['y1'] < r2['y1']   and r1['x2'] > r2['x2']  and r1['y2'] > r2['y2']):
        return False
    if (r2['x1'] > r1['x2'] or r2['x2'] < r1['x1'] or r2['y1'] > r1['y2'] or r2['y2'] < r1['y1']):
        return False
    return True
N = int(input())

rect = [{
        'x1' : 0,
        'x2' : 0,
        'y1' : 0,
        'y2' : 0
    }]
for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    rect.append({
        'x1' : x1,
        'x2' : x2,
        'y1' : y1,
        'y2' : y2
    })
make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]


for i in range(N+1):
    for j in range(N+1):
        if i != j and connect(rect[i],rect[j]):
            if find_parents(i) != find_parents(j):
                union(i,j)


for ind in range(N):
    find_parents(ind)


print(len(set(make_set))-1)