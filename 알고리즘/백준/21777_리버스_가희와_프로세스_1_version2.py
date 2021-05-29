# jthis님 풀이

import sys

input = sys.stdin.readline
N = int(input())
process_state = [[0 for _ in range(2)] for _ in range(1000001)]
# 0번 인덱스 총 시간
# 1번 인덱스 우선순위
arr = list(map(int,input().split()))

total_process = 0
for i in range(N):
    cur_process = arr[i]
    if not process_state[cur_process][0]:
        total_process += 1
    process_state[cur_process][0] += 1
 


pre_priority = 1
last_value = arr[-1]
process_state[last_value][1] = 1

for i in range(N-2,-1,-1):
    cur_process = arr[i]
    if not process_state[cur_process][1]:
        # 처음 나왔을때
        if cur_process<last_value:
            process_state[cur_process][1] = pre_priority
            # 이후의 값보다 낮은 값이면, 같은 순증가이므로, 같은 우선순위
        else:
            process_state[cur_process][1] = pre_priority + 1
    else:
        process_state[cur_process][1] += 1

    
    pre_priority = process_state[cur_process][1]
    last_value = cur_process


sys.stdout.write(str(total_process)+'\n')

for i in range(1000001):
    if process_state[i][0]:
        sys.stdout.write(str(i)+' '+str(process_state[i][0])+' '+str(process_state[i][1])+'\n')

