import heapq
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())


skylines = []

for idx in range(1,N+1):
    left,height,right = map(int,input().split())
    skylines.append((left,height,idx))
    skylines.append((right,-height,idx))
skylines.append((float('inf'),float('inf')))
skylines.sort()
idx = 0
last_x = skylines[0][0]
last_y = -1
height_list = [(0,0)]
remove_idx = set()
while idx<2*N:
    while last_x == skylines[idx][0]:
        cur_x,cur_height,cur_idx = skylines[idx]
        if cur_height<0:
            remove_idx.add(cur_idx)
        else:
            heapq.heappush(height_list,(-cur_height,cur_idx))
        idx += 1
    while height_list and height_list[0][1] in remove_idx:
        heapq.heappop(height_list)
    max_height = -height_list[0][0] 
    if last_y != max_height:
        print(last_x,max_height,end=' ')
        last_y = max_height
    last_x = skylines[idx][0]