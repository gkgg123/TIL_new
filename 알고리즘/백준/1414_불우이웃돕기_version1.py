import sys
import heapq
def convert_Numner(x):
    global total_sum,INF
    if x.islower():
        num = ord(x) - ord('a') + 1
        total_sum += num
    elif x.isupper():
        num = ord(x) - ord('A')+ 27
        total_sum += num
    else:
        num = INF
        total_sum += 0
    return num


def input():
    return sys.stdin.readline().rstrip()


N = int(input())


total_sum = 0
INF = float('inf')
arr = [list(map(convert_Numner,list(input()))) for _ in range(N)]


cnt = 0
mst_dis = 0
distance_list = [INF for _ in range(N)]
visited = [False for _ in range(N)]
node_list = []

heapq.heappush(node_list,(0,0))
distance_list[0] = 0
while node_list:
    cur_dis,cur_node = heapq.heappop(node_list)
    if visited[cur_node]:continue
    cnt += 1
    mst_dis += cur_dis
    visited[cur_node] = True
    for next_node in range(N):
        if visited[next_node]:continue
        min_value = min(arr[cur_node][next_node],arr[next_node][cur_node])
        if distance_list[next_node] > min_value:
            distance_list[next_node] = min_value
            heapq.heappush(node_list,(min_value,next_node))

if cnt == N:
    print(total_sum-mst_dis)
else:
    print(-1)


