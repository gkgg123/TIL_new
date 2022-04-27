import sys
from collections import defaultdict,deque
import heapq
def input():
    return sys.stdin.readline().rstrip()

N,K = map(int,input().split())

key_dict = defaultdict(deque)
arr =  list(map(int,input().split()))
for ind in range(K):
    num = arr[ind]
    key_dict[num].append(ind)
multitap = set()
remove_ind = []
answer = 0
past_ind = set()
for cur_num in arr:
    if cur_num in multitap or len(multitap)<N:
        multitap.add(cur_num)
        prev_ind = key_dict[cur_num].popleft()
        past_ind.add(prev_ind)
        if key_dict[cur_num]:
            heapq.heappush(remove_ind,(-key_dict[cur_num][0],cur_num))
        else:
            heapq.heappush(remove_ind, (-float('inf'),cur_num))
    else:
        while True:
            pop_ind,remove_num = heapq.heappop(remove_ind)
            if pop_ind not in past_ind:
                break
        multitap.remove(remove_num)
        multitap.add(cur_num)
        prev_ind = key_dict[cur_num].popleft()
        past_ind.add(prev_ind)
        if key_dict[cur_num]:
            heapq.heappush(remove_ind,(-key_dict[cur_num][0],cur_num))
        else:
            heapq.heappush(remove_ind, (-float('inf'),cur_num))
        answer += 1
print(answer)