import sys
input = sys.stdin.readline
def find_pedigrees(node,dep):
    pedigree[node] = []

    for child in childs_dict[node]:
        if parents_cnt[child] == dep:
            pedigree[node].append(child)
            find_pedigrees(child,dep+1)


N = int(input())


names = list(input().split())

parents_cnt = {i : 0 for i in names}
parents_dict = {i : [] for i in names}
childs_dict = {i : [] for i in names}
M = int(input())
for _ in range(M):
    A,B = input().split()
    parents_cnt[A] += 1
    parents_dict[A].append(B)
    childs_dict[B].append(A)

root_nodes =  []
pedigree = {}
for parent in parents_cnt.keys():
    if parents_cnt[parent] == 0:
        root_nodes.append(parent)
print(len(root_nodes))
print(*sorted(root_nodes))
for name in root_nodes:
    find_pedigrees(name,1)

for name in sorted(pedigree.keys()):
    if pedigree[name]:
        print(name,len(pedigree[name]),*sorted(pedigree[name]))
    else:
        print(name,0)