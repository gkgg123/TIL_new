import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]


arr.sort()
heap = []
result = 0
range_result = [0,0]
for start_time,end_time in arr:
    if heap and heap[0][0] <= start_time:
        # 가장 작은 모기 퇴장시간보다 새로운 모기 입장시간이 더 느리거나 같으면, 없는 모기이므로 pop
        heapq.heappop(heap)
    heapq.heappush(heap,(end_time,start_time))

    if len(heap) == result and start_time == range_result[1]:
        range_result[1] = heap[0][0]
    elif len(heap) > result:
        result = len(heap)
        range_result = [start_time,heap[0][0]]

print(result)
print(*range_result)