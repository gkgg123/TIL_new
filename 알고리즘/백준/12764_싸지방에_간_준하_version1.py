import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
init_list = [list(map(int,input().split())) for _ in range(N)]

init_list.sort()
result = [0 for _ in range(100001)]
INF = float('inf')
for start_time,end_time in init_list:
    if heap:
        if heap[0] <= start_time:
            heapq.heappop(heap)
        heapq.heappush(heap,end_time)
    else:
        heapq.heappush(heap,end_time)
total_cnt = len(heap)
print(total_cnt)

check_number = []
min_chair_number = []
for start_time,end_time in init_list:
    if check_number:
        while check_number and check_number[0][0] <= start_time:
            _,pop_idx = heapq.heappop(check_number)
            heapq.heappush(min_chair_number,pop_idx)
        if not min_chair_number:
            idx = len(check_number)
            heapq.heappush(check_number,(end_time,idx))
            result[idx] += 1
        else:
            idx = heapq.heappop(min_chair_number)
            heapq.heappush(check_number,(end_time,idx))
            result[idx] += 1
    else:
        result[0] += 1
        heapq.heappush(check_number,(end_time,0))
print(*result[:total_cnt])