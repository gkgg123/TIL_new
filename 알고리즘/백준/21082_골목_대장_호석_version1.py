import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

def check(mid):
    node_list = []
    INF = float('inf')
    heapq.heappush(node_list,(0,A))
    distance = [INF for _ in range(N+1)]
    distance[A] = 0
    while node_list:
        cur_pay,cur_node = heapq.heappop(node_list)
        if distance[cur_node]<cur_pay:
            continue
        if cur_node == B:
            break
        for next_node in grpah[cur_node]:
            if grpah[cur_node][next_node] + cur_pay < distance[next_node] and grpah[cur_node][next_node]<=mid:
                distance[next_node] = grpah[cur_node][next_node]+cur_pay
                heapq.heappush(node_list,(distance[next_node],next_node))
    if distance[B]<=C:
        return True
    return False


N,M,A,B,C = map(int,input().split())
grpah = [{} for i in range(N+1)]
left = 0
right = 0
for _ in range(M):
    x,y,pay = map(int,input().split())
    grpah[x][y] = pay
    grpah[y][x] = pay
    right = max(right,pay)
if check(right):
    while left+1<right:
        mid = (left+right)//2
        if check(mid):
            right = mid
        else:
            left = mid
    print(right)
else:
    print(-1)

