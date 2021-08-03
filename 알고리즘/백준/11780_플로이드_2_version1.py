import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()
def path(s,e):
    if next_node[s][e] == None:
        return [0]
    else:
        result = [s]
        while s != e:
            s = next_node[s][e]
            result.append(s)
        return result
N = int(input())
M = int(input())
INF = float('inf')
distance_list = [[0 if i==j else INF for j in range(N+1)] for i in range(N+1)]

next_node = [[None for _ in range(N+1)] for _ in range(N+1)]
graph = [{} for _ in range(N+1)]
for _ in range(M):
    x,y,pay = map(int,input().split())
    if distance_list[x][y] > pay:
        distance_list[x][y] = pay
        next_node[x][y] = y


for mid in range(1,N+1):
    for start in range(1,N+1):
        for end in range(1,N+1):
            if distance_list[start][end] > distance_list[start][mid] + distance_list[mid][end]:
                distance_list[start][end] = distance_list[start][mid] + distance_list[mid][end]
                next_node[start][end] = next_node[start][mid]


for i in range(1,N+1):
    print(*[val if val != INF else 0 for val in distance_list[i][1:]])


for start in range(1,N+1):
    for ends in range(1,N+1):
        if distance_list[start][ends] == INF:
            print(0)
        else:
            answer = path(start,ends)
            if len(answer) == 1:
                print(0)
            else:
                print(len(answer),*answer)