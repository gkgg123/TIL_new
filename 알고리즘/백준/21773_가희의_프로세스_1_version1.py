import heapq
import sys
input = sys.stdin.readline

T,N = map(int,input().split())

heap_list = []


for _ in range(N):
    id_num,times,C = map(int,input().split())
    heapq.heappush(heap_list,(-C,id_num,times))

result = []
for _ in range(T):

    prioty,id_num,times = heapq.heappop(heap_list)
    times -= 1
    result.append(id_num)
    if times != 0:
        heapq.heappush(heap_list,(prioty+1,id_num,times))


for i in range(T):
    sys.stdout.write(str(result[i])+'\n')