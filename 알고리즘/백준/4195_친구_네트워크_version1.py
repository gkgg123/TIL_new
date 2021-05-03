import sys
input = sys.stdin.readline
def union_find(x,y):
    a = find_parent(x)
    b = find_parent(y)
    if a != b:
        make_set[b] = a
        friend_cnt[a] += friend_cnt[b]

    return a

def find_parent(A):
    if make_set[A] == A:
        return A
    make_set[A] = find_parent(make_set[A])
    return make_set[A]


T = int(input())

for tc in range(T):
    F = int(input())
    person_dict = {}
    cnt = 1
    make_set = [k for k in range(F*2+1)]
    friend_cnt = [1 for k in range(F*2+1)]
    for _ in range(F):
        x,y = input().split()
        if x not in person_dict:
            person_dict[x] = cnt
            friend_cnt[person_dict[x]] = 1
            cnt += 1
        if person_dict.get(y) == None:
            person_dict[y] = cnt
            friend_cnt[person_dict[y]] = 1
            cnt += 1
        x_num = person_dict[x]
        y_num = person_dict[y]
        k = union_find(x_num,y_num)
        print(friend_cnt[k])