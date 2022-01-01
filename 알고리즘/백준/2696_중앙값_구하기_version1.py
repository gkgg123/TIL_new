import sys
import heapq
import math
def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(math.ceil(N/10)):
        temp = list(map(int,input().split()))
        arr.extend(temp)
    min_heap = []
    max_heap = []
    result = [[]]
    for idx,val in enumerate(arr):
        if len(min_heap) == len(max_heap):
            heapq.heappush(max_heap,-val)
        else:
            heapq.heappush(min_heap,val)
        if min_heap and max_heap and min_heap[0] < -max_heap[0]:
            max_number = -heapq.heappop(max_heap)
            min_number = heapq.heappop(min_heap)
            heapq.heappush(max_heap,-min_number)
            heapq.heappush(min_heap,max_number)
        if not idx%2:
            if len(result[-1])<10:
                result[-1].append(-max_heap[0])
            else:
                result.append([-max_heap[0]])
    print((N+1)//2)
    for row in result:
        print(*row)