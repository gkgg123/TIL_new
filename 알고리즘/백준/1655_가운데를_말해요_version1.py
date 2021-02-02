import heapq
import sys
N = int(input())


max_heapq = []
min_heapq = []
for _ in range(N):
    number = int(sys.stdin.readline())
    if len(max_heapq) == len(min_heapq):
        heapq.heappush(max_heapq,-number)
    else:
        heapq.heappush(min_heapq,number)
    if min_heapq and max_heapq and min_heapq[0] < -max_heapq[0]:
        max_number = -heapq.heappop(max_heapq)
        min_number = heapq.heappop(min_heapq)

        heapq.heappush(max_heapq,-min_number)
        heapq.heappush(min_heapq,max_number)
    print(-max_heapq[0])