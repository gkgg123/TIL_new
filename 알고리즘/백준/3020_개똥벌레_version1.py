# 3020 개똥벌레

N,H = map(int,input().split())

bottom_list = [0]*H
top_list = [0]*H


for ind in range(N):
    height = int(input())
    if ind%2:
        top_list[height] += 1
    else:
        bottom_list[height] += 1

for ind in range(1,H):
    bottom_list[ind] += bottom_list[ind-1]
    top_list[ind] += top_list[ind-1] 

bottom_list.append(bottom_list[-1])
top_list.append(top_list[-1])
min_result = float('inf')
min_cnt = 0
for k in range(H):
    bottom_cnt = bottom_list[-1] - bottom_list[k]
    top_cnt = top_list[-1] - top_list[(H-1)-k]
    if bottom_cnt +top_cnt < min_result:
        min_result = bottom_cnt+top_cnt
        min_cnt = 1
    elif bottom_cnt + top_cnt == min_result:
        min_cnt += 1

print(min_result,min_cnt)