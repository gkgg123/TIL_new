import sys

input = sys.stdin.readline
N = 1000001

T = int(input())
INF = float('inf')
start_process_time = [INF]*N
end_process_time = [0]*N
arr = list(map(int,input().split()))
mono_times = 1
prev_process = -1
for i in range(T):
    cur_process = arr[i]
    if prev_process >= cur_process:
        mono_times += 1

    start_process_time[cur_process] = min(start_process_time[cur_process],mono_times)
    end_process_time[cur_process] = max(end_process_time[cur_process],mono_times)
    prev_process = cur_process


active_process_list = []
for i in range(N):
    if end_process_time[i]:
        active_process_list.append(i)



result = []
for process_id in active_process_list:
    priority = N-1-start_process_time[process_id]
    spend_time = end_process_time[process_id]-start_process_time[process_id] + 1
    result.append((str(process_id),str(spend_time),str(priority)))


sys.stdout.write(str(len(active_process_list))+'\n')


for i in range(len(active_process_list)):
    sys.stdout.write(' '.join(result[i])+'\n')
