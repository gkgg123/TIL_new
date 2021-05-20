import sys

input = sys.stdin.readline

def find_parent(idx):
    if idx == make_set[idx]:
        return idx
    else:
        make_set[idx] = find_parent(make_set[idx])
        return make_set[idx]

G = int(input())
P = int(input())

make_set = [i for i in range(G+1)]


result = 0
for k in range(P):
    plane_num = int(input())
    gate_num = find_parent(plane_num)

    if gate_num < 1:
        break
    else:
        make_set[gate_num] = make_set[gate_num-1]
        result += 1
        

print(result)