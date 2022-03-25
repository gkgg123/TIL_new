import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()



N = int(input())

time_dict = defaultdict(int)
for _ in range(N):
    x,y = map(int,input().split())
    time_dict[x] += 1
    time_dict[y] -= 1


max_ind = len(time_dict.keys())

prefix_sum = [0 for _ in range(max_ind+1)]
time_mapping = {}
time_list = sorted(time_dict.keys())

for ind,time in enumerate(time_list):
    prefix_sum[ind+1] = time_dict[time]
    time_mapping[ind+1] = time

max_cnt = 0
max_time = []
flag = False

for ind in range(1,max_ind+1):
    prefix_sum[ind] += prefix_sum[ind-1]
    if prefix_sum[ind] > max_cnt:
        max_cnt = prefix_sum[ind]
        flag = True
        max_time = [time_mapping[ind]]
    elif flag and max_cnt>prefix_sum[ind]:
        flag = False
        max_time.append(time_mapping[ind])
print(max_cnt)
print(*max_time)