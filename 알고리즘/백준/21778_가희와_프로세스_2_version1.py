import sys
input = sys.stdin.readline
INF = (10**12)+1

def get_process(mid_priority):
    global N
    if dp.get(mid_priority):
        return dp[mid_priority]
    else:
        total_process_cnt = 0


        for i in range(N):
            process = arr[i]

            if mid_priority<=process.sp:
                total_process_cnt += process.time
            elif process.sp< mid_priority<=process.ep:
                total_process_cnt = total_process_cnt + process.ep - mid_priority +1
        
        dp[mid_priority] = total_process_cnt
        return total_process_cnt


def b_search(target_T):
    left = 0
    right = INF*2
    while left<=right:
        mid = (left+right)//2
        total_cnt = get_process(mid)
        if total_cnt>=target_T:
            next_priority_cnt = get_process(mid+1)
            if next_priority_cnt<target_T:
                remain_priority_cnt = target_T - next_priority_cnt
                for i in range(N):
                    if arr[i].sp <= mid <=arr[i].ep:
                        remain_priority_cnt -= 1
                        if remain_priority_cnt == 0:
                            result.append(arr[i].process_id)
                            break
                break
            else:
                left = mid + 1

        else:
            right = mid-1


class Process:
    def __init__(self,_id,_spend_time,_init_priority):
        self.process_id = _id
        self.time = _spend_time
        self.ep = _init_priority+INF
        self.sp = _init_priority+INF-spend_time+1


Q,N = map(int,input().split())
arr = []
for _ in range(N):
    process_id,spend_time,init_priority = map(int,input().split())
    new_process = Process(process_id,spend_time,init_priority)
    arr.append(new_process)
dp = {}
arr.sort(key=lambda x : x.process_id)
result = []

for _ in range(Q):
    find_time = int(input())

    b_search(find_time)


for i in range(Q):
    sys.stdout.write(str(result[i])+'\n')