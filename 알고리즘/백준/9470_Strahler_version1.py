import sys
from collections import deque,defaultdict
input = sys.stdin.readline
# 강의 근원 노드의 순서는 1이다.

T = int(input())

for _ in range(T):
    K,M,P = map(int,input().split())
    # K case의 번호
    # M은 노드의 수
    # P는 간선의 수

    strahelr_dict = [defaultdict(int) for _ in range(M+1)]
    strahelr_list = [-1 for _ in range(M+1)]
    graph = [[] for _ in range(M+1)]
    indegree_list = [0 for _ in range(M+1)]
    for _ in range(P):
        x,y = map(int,input().split())
        graph[x].append(y)
        indegree_list[y] += 1
    stack = deque()
    for i in range(1,M+1):
        if not indegree_list[i]:
            stack.append(i)
            strahelr_list[i] = 1
    
    while stack:

        node = stack.popleft()
        cur_strahler = strahelr_list[node]
        for next_node in graph[node]:
            indegree_list[next_node] -= 1
            strahelr_dict[next_node][cur_strahler] += 1
            if not indegree_list[next_node]:
                stack.append(next_node)
                next_strahelr = max(strahelr_dict[next_node].keys())
                if strahelr_dict[next_node][next_strahelr] > 1:
                    strahelr_list[next_node] = next_strahelr + 1
                else:
                    strahelr_list[next_node] = next_strahelr



    print(K,strahelr_list[M])
