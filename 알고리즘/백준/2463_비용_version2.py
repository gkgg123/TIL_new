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
        groups[X] +=groups[Y]
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True
    return False
N,M = map(int,input().split())


edge_list = []
total_pay = 0
for _ in range(M):
    x,y,pay = map(int,input().split())
    if x>y:
        x,y = y,x
    edge_list.append((x,y,pay))
    total_pay += pay
K = 10**9
past_pay = 0
answer = 0
make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]
groups = [ 1 for _ in range(N+1)]
edge_list.sort(key=lambda x : x[2])
while edge_list:
    x,y,pay = edge_list.pop()
    p_x,p_y = find_parents(x),find_parents(y)
    if p_x!= p_y:
        answer = answer + groups[p_x]*groups[p_y]*(total_pay-past_pay)
        answer = answer%K
        union(p_x,p_y)
    past_pay += pay
print(answer)
