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



N = int(input())
edge_list = []
for x in range(N):
    temp = list(map(int,input().split()))
    for y in range(N):
        if x == y:continue
        edge_list.append((temp[y],x,y))


edge_list.sort(reverse=True)

cnt = 1
make_set = [i for i in range(N)]
ranks = [1 for _ in range(N)]
result = 0
while cnt <N:
    dis,node_a,node_b = edge_list.pop()
    if union(node_a,node_b):
        cnt += 1
        result += dis

print(result)
