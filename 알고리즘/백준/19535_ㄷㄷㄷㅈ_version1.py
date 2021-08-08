import sys
from itertools import combinations
import math
def input():
    return sys.stdin.readline().rstrip()



N = int(input())

graph = [[] for _ in range(N+1)]


for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

d_cnt = 0
g_cnt = 0


for i in range(1,N+1):
    if len(graph[i])>=3:
        k = len(graph[i])
        cnt = math.factorial(k)/(math.factorial(3)*math.factorial(k-3))
        g_cnt += cnt
    if len(graph[i])>=2:
        for next_node in graph[i]:
            if len(graph[next_node])>=2:
                a = len(graph[i]) - 1
                b = len(graph[next_node]) - 1
                d_cnt += (a*b)

d_cnt//=2

if d_cnt > g_cnt*3:
    print('D')
elif d_cnt < g_cnt*3:
    print('G')
else:
    print('DUDUDUNGA')