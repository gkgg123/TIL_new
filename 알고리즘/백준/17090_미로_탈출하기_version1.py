import sys

def input():
    return sys.stdin.readline()

N,M = map(int,input().split())

def find_parents(X):
    if X == make_set[X]:
        return X
    make_set[X] = find_parents(make_set[X])
    return make_set[X]


def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)

    if X !=Y:
        if ranks[X]< ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        cnt[X] += cnt[Y]
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True
    return False
dire = {
    "U": [-1,0],
    "L": [0,-1],
    "R" : [0, 1],
    'D': [1,0]
}

arr = [list(input()) for _ in range(N)]
make_set = [i for i in range(N*M+1)]
ranks = [1 for _ in range(N*M+1)]
cnt = [1 for _ in range(N*M+1)]
ranks[N*M] = float('inf')

for x in range(N):
    for y in range(M):
        point = x*M+y
        dx,dy = dire[arr[x][y]]
        nx = x + dx
        ny = y + dy

        if 0<=nx<N and 0<=ny<M:
            next_point = (x+dx)*M+y+dy
            union(point,next_point)
        else:
            union(point,N*M)
print(cnt[N*M]-1)