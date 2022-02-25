import sys
def input():
    return sys.stdin.readline().rstrip()


def cal(ind1,ind2):
    x1,y1 = citys[ind1]
    x2,y2 = citys[ind2]
    return abs(x1-x2) + abs(y1-y2)

def find(node):
    min_idx = -1
    min_val = float('inf')
    for next_node in range(N):
        if next_node not in special:
            continue
        if min_val > dis[node][next_node]:
            min_val = dis[node][next_node]
            min_idx = next_node
    return min_idx



def solve(a,b):
    cur_dis = dis[a][b]

    min_a_idx = find(a)
    min_b_idx = find(b)

    if min_a_idx != -1 and min_b_idx != -1:
        return min(cur_dis,dis[a][min_a_idx] + T + dis[min_b_idx][b])
N,T = map(int,input().split())


citys = []
special = set()
INF = float('inf')
dis = [[INF if i!=j else 0 for j in range(N)] for i in range(N)]
for ind in range(N):
    k,x,y = map(int,input().split())
    citys.append((x,y))
    if k:
        special.add(ind)

for x in range(N):
    for y in range(N):
        if x in special and y in special:
            dis[x][y] = min(cal(x,y),T)
        else:
            dis[x][y] = cal(x,y)



M = int(input())

for _ in range(M):
    a,b = map(int,input().split())
    print(solve(a-1,b-1))