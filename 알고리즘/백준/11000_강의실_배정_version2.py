import heapq
import sys
input = sys.stdin.readline

N = int(input())
class_list = []
for _ in range(N):
    start_time,end_time = map(int,input().split())
    class_list.append((start_time,end_time))

class_list.sort()
end_time_list = []
for start_time,end_time in class_list:
    if end_time_list:
        if end_time_list[0] <= start_time:
            heapq.heappop(end_time_list)
        heapq.heappush(end_time_list,end_time)
    else:
        heapq.heappush(end_time_list,end_time)

print(len(end_time_list))

