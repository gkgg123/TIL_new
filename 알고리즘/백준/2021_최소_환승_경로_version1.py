import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())


graph = [[] for _ in range(N+1)]



for ind in range(M):
    arr = list(map(int,input().split()))
    lens = len(arr)

    for arr_ind in range(lens-1):
        cur_node = arr[arr_ind]
        if arr_ind == 0:
            graph[cur_node].append([-1,arr[arr_ind+1],ind])
        else:
            graph[cur_node].append([arr[arr_ind-1],arr[arr_ind+1],ind])

start_node, end_node = map(int,input().split())
INF = float('inf')
distance_list = [INF for _ in range(N+1)]
visited_node = [True for _ in range(N+1)]
distance_list[start_node] = 0
queue = deque()

queue.append((start_node,0,-1))

while queue:
    node,cnt,prev_ind = queue.popleft()
    for left_node,right_node,position in graph[node]:
        if left_node != -1:
            if prev_ind == -1:
                distance_list[left_node] = cnt
                queue.append((left_node,cnt,position))
            else:
                temp = 1 if prev_ind != position else 0
                if distance_list[left_node] > cnt + temp:
                    distance_list[left_node] = cnt + temp
                    queue.append((left_node,cnt+temp,position))
        if right_node != -1:
            if prev_ind == -1:
                distance_list[right_node] = cnt
                queue.append((right_node,cnt,position))
            else:
                temp = 1 if prev_ind != position else 0
                if distance_list[right_node] > cnt + temp:
                    distance_list[right_node] = cnt + temp
                    queue.append((right_node,cnt+temp,position))




if distance_list[end_node] == INF:
    print(-1)
else:
    print(distance_list[end_node])