# 42_jakang님 풀이
import sys
input = sys.stdin.readline


def tree_dp(cur_node):

    if not len(graph[cur_node]):
        strahler_list[cur_node] = 1
        return
    else:
        max_st_cnt = 0
        for parent_node in graph[cur_node]:
            tree_dp(parent_node)

            if strahler_list[cur_node] < strahler_list[parent_node]:
                strahler_list[cur_node] = strahler_list[parent_node]
                max_st_cnt = 1
            elif strahler_list[cur_node] == strahler_list[parent_node]:
                max_st_cnt += 1
        if max_st_cnt > 1:
            strahler_list[cur_node] += 1
T = int(input())

for _ in range(T):
    K,M,P = map(int,input().split())
    strahler_list = [0 for _ in range(M+1)]
    graph = [[] for _ in range(M+1)]

    for _ in range(P):
        x,y = map(int,input().split())
        graph[y].append(x)

    

    tree_dp(M)
    print(K,strahler_list[M])
    