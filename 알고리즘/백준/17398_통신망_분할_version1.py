import sys

input = sys.stdin.readline


def find_parent(ind):
    if make_set[ind] == ind:
        return ind
    else:
        make_set[ind] = find_parent(make_set[ind])
        return make_set[ind]

def union(x,y):
    X = find_parent(x)
    Y = find_parent(y)
    if X == Y:
        return 0

    else:
        if rank[X] < rank[Y]:
            X,Y = Y,X

        size_a,size_b = rank[X],rank[Y]
        rank[X] += rank[Y]
        make_set[Y] = X
        return size_a*size_b
            
        

N,M,Q = map(int,input().split())



make_set = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]
connect_input = [[],]
check = [True]*(M+1)
for _ in range(M):
    x,y = map(int,input().split())
    connect_input.append((x,y))

result = 0
disconnet_list = []

for _ in range(Q):
    ind = int(input())
    disconnet_list.append(ind)
    check[ind] = False


for i in range(1,M+1):
    if check[i]:
        x,y = connect_input[i]
        union(x,y)


while disconnet_list:
    ind = disconnet_list.pop()
    x,y = connect_input[ind]
    result += union(x,y)
print(result)