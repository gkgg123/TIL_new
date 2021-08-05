import sys
def convert(k):
    if len(k) == 1:
        return '0'+k
    return k
def input():
    return sys.stdin.readline().rstrip()

start_time = list(map(int,input().split(':')))

start_time = start_time[0]*3600+start_time[1]*60+start_time[0]
N = int(input())

operating_time = {1:3,
12 : 4,
16 : 3,
36:4,
40:4,
47:3,
11:4,
13:3,
29:3,
38:5,
41:3,
57:3}
min_k = 209
goal = 272-min_k
start_node = 225 - min_k
arr = []
for _ in range(N):
    x,y,time = input().split()
    x = int(x[1:]) - min_k
    y = int(y[1:]) - min_k
    hour,mins = map(int,time.split(':'))
    total_time = hour*3600 + mins*60 + 0

    arr.append([x,y,total_time])


time_table = [0 for _ in range(goal+1)]

for k in range(goal):
    if k not in operating_time:
        time_table[k+1] = time_table[k] + 2*60+20
    else:
        time_table[k+1] = time_table[k] + operating_time[k]*60+20
INF = 25*3600
result = [[INF, INF] for _ in range(5)]
result[0][0] = start_time
k = 0
flag = True
prev_node = start_node
stop_node_list = [24, 37, 49, 63]
while stop_node_list:
    next_node = stop_node_list.pop(0)
    min_time = INF
    for ind in range(N):
        train_start_node,train_end_node,train_start_time = arr[ind]
        if prev_node>=train_end_node or prev_node<train_start_node:
            continue

        arrive_time = train_start_time + time_table[prev_node]-time_table[train_start_node]
        if result[k][0] < arrive_time < min_time:
            min_time = arrive_time
    if min_time == INF:
        flag = False
        break
    next_time = min_time + time_table[next_node] - time_table[prev_node]-20
    result[k][1] = next_time
    k += 1
    result[k][0] = result[k-1][1]
    prev_node = next_node


if flag:
    if result[-1][0] < 86400:
        hour = str(result[-1][0]//3600)
        mins = str(result[-1][0]%3600//60)
        sec = str(result[-1][0]%3600%60)
        hour = convert(hour)
        mins = convert(mins)
        sec = convert(sec) 
        print(f'{hour}:{mins}:{sec}')
    else:
        print(-1)
else:
    print(-1)

