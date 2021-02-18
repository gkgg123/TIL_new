# 3020 개똥벌레
import sys


N,H = map(int,sys.stdin.readline().split())

bottom_list = [0]*(H+1)
top_list = [0]*(H+1)

for ind in range(N):
    height = int(input())
    if ind%2:
        top_list[height] += 1
    else:
        bottom_list[H-height+1] += 1
for ind in range(H-1,0,-1):
    top_list[ind] += top_list[ind+1]


for ind in range(2,H+1):
    bottom_list[ind] += bottom_list[ind-1]

min_total = N
min_cnt = 0
for ind in range(1,H+1):
    sub_sum = bottom_list[ind] + top_list[ind]
    if sub_sum < min_total:
        min_total = sub_sum
        min_cnt = 1
    elif sub_sum == min_total:
        min_cnt += 1
print(min_total,min_cnt)
