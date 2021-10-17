import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
node = []
time = []
for _ in range(N):
    num,s,e = map(int,input().split())
    time.append((s,e))

time.sort()
answer = []
for start_time,end_time in time:
    if answer:
        if answer[0] <= start_time:
            heapq.heappop(answer)
        heapq.heappush(answer,end_time)
    else:
        heapq.heappush(answer,end_time)
print(len(answer))