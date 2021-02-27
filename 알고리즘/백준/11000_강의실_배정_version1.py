import heapq
import sys
input = sys.stdin.readline
N = int(input())

times = []
for _ in range(N):
    input_tuple = tuple(map(int,input().split()))
    heapq.heappush(times,input_tuple)

end_time_list = []
answer = 0
while times:
    start_time,end_time = heapq.heappop(times)
    if not end_time_list:
        answer += 1
        heapq.heappush(end_time_list,end_time)
    else:
        if end_time_list[0] > start_time:
            heapq.heappush(end_time_list,end_time)
            answer += 1
        else:
            heapq.heappop(end_time_list)
            heapq.heappush(end_time_list,end_time)
            
        
print(answer)