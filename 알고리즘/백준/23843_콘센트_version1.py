import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
arr = list(map(int,input().split()))
max_heap = []
arr.sort(reverse=True)
for t in arr:
    if len(max_heap)<M:
        heapq.heappush(max_heap,t)
    else:
        last = heapq.heappop(max_heap)
        heapq.heappush(max_heap,last+t)
print(max(max_heap))