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
        if ranks[X]< ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True
    return False


T = int(input())


for tc in range(1,T+1):
    N = int(input())
    make_set = [i for i in range(N)]
    ranks = [1 for _ in range(N)]

    for _ in range(int(input())):
        x,y = map(int,input().split())
        union(x,y)
    print(f'Scenario {tc}:')
    for _ in range(int(input())):
        x,y = map(int,input().split())
        if find_parents(x) != find_parents(y):
            print(0)
        else:
            print(1)

    if tc != T:
        print()