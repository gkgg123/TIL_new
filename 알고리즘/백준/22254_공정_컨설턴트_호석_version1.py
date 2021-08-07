import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def check(mid):
    stack = times[:mid]
    heapq.heapify(stack)
    for cur_time in times[mid:]:
        accu_time = heapq.heappop(stack)
        if accu_time>X:
            return False
        if accu_time + cur_time > X:
            return False
        heapq.heappush(stack,accu_time+cur_time)
    return True



N,X = map(int,input().split())

times = list(map(int,input().split()))


left = 0
right = N

while left+1<right:
    mid = (left+right)//2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)