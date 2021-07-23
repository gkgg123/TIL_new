import sys
from collections import deque

def input():
    return sys.stdin.readline()

N,T,W = map(int,input().split())

waiting_list = deque([list(map(int,input().split())) for _ in range(N)])

M = int(input())

oncomming_list = [list(map(int,input().split())) for _ in range(M)]
oncomming_list.sort(key=lambda x : -x[2])
time = 0
result = []
flag = False
while time<W:
    pid,consumer_time = waiting_list.popleft()
    spend_time = T if consumer_time>T else consumer_time

    for k in range(spend_time):
        result.append(pid)
        time += 1
        if  time == W:
            flag = True
            break
        if oncomming_list:
            if time == oncomming_list[-1][2]:
                new_pid,new_spend_time,_ = oncomming_list.pop()
                waiting_list.append((new_pid,new_spend_time))
    if consumer_time != spend_time:
        waiting_list.append((pid,consumer_time-spend_time))
    if flag:
        break


for answer in result:
    sys.stdout.write(f'{answer}\n')
