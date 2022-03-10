from audioop import reverse
import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(node):
    childs_size = []

    for child_node in childs[node]:
        childs_size.append(dfs(child_node))

    spend_time = 0
    childs_size.sort(reverse=True)
    addition_time = 0
    for time in childs_size:
        spend_time = max(spend_time, time + addition_time + 1)
        addition_time += 1
    return spend_time

N = int(input())


parents = list(map(int,input().split()))
childs = [[] for _ in range(N)]
for i in range(1,N):
    p,c = parents[i],i
    childs[p].append(c)


answer =  dfs(0)

print(answer)