import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

times = []

N = int(input())
for _ in range(N):
    num,s,e = map(int,input().split())
    times.append((s,e))

heapq.heapify(times)
end_time_list = []
answer = 0
while times:
    s, e = heapq.heappop(times)
    if not end_time_list:
        answer += 1
        heapq.heappush(end_time_list,e)
    else:
        if end_time_list[0] > s:
            heapq.heappush(end_time_list,e)
            answer += 1
        else:
            heapq.heappop(end_time_list)
            heapq.heappush(end_time_list,e)
print(answer)