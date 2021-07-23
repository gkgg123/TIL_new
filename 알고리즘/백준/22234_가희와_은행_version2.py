import sys
from collections import deque
import heapq

N,T,W = map(int,input().split())




waiting_list = deque([list(map(int,input().split())) for _ in range(N)])

M = int(input())
oncomming_list = []
for _ in range(M):
    pid,spend_time,on_time = map(int,input().split())
    oncomming_list.append((on_time,pid,spend_time))

heapq.heapify(oncomming_list)
time = 0
result = []
while time<W:
    pid,consumer_time = waiting_list.popleft()
    spend_time = T if consumer_time >T else consumer_time

    result.extend([pid]*spend_time)
    time += spend_time
    if oncomming_list:
        while oncomming_list and oncomming_list[0][0] <=time:
            _,new_pid,new_consumer_time = heapq.heappop(oncomming_list)
            waiting_list.append((new_pid,new_consumer_time))
    
    if spend_time != consumer_time:
        waiting_list.append((pid,consumer_time-spend_time))


for ind in range(W):
    sys.stdout.write(f'{result[ind]}\n')