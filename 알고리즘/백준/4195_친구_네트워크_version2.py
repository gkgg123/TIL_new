import sys

def union_find(X,Y):
    x = find_parent(X)
    y = find_parent(Y)
    if x != y:
        make_set[y] = x
        friend_cnt[x] += friend_cnt[y]
    return x

def find_parent(ind):
    if make_set[ind] == ind:
        return ind
    else:
        new_parent = find_parent(make_set[ind])
        make_set[ind] = new_parent
        return new_parent



T = int(input())


for _ in range(T):
    F = int(input())


    make_set = {}
    friend_cnt = {}

    for _ in range(F):
        a,b = map(str,input().split())


        if make_set.get(a) == None:
            make_set[a] = a
            friend_cnt[a] = 1
        if make_set.get(b) == None:
            make_set[b] = b
            friend_cnt[b] = 1

        k = union_find(a,b)
        print(friend_cnt[k])