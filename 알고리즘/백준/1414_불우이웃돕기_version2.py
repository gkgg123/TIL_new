import sys
def convert_Numner(x):
    global total_sum,INF
    if x.islower():
        num = ord(x) - ord('a') + 1
        total_sum += num
    elif x.isupper():
        num = ord(x) - ord('A')+ 27
        total_sum += num
    else:
        num = INF
        total_sum += 0
    return num


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

def input():
    return sys.stdin.readline().rstrip()

N = int(input())


total_sum = 0
INF = float('inf')


edge_list = []
for x in range(N):
    input_string = input()
    temp = []
    for y in range(N):
        num = convert_Numner(input_string[y])
        if x == y:continue
        if num == INF:continue
        edge_list.append((num,x,y))
edge_list.sort(reverse=True)
cnt = 1
result = 0
make_set = [i for i in range(N)]
ranks = [1 for _ in range(N)]
while cnt <N and edge_list:
    pay,node_a,node_b = edge_list.pop()
    if union(node_a,node_b):
        cnt += 1
        result += pay


if cnt == N:
    print(total_sum-result)
else:
    print(-1)