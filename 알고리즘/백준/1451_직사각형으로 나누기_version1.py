

import re
import sys
def input():
    return sys.stdin.readline().rstrip()

def area_sum(x1,y1,x2,y2):
    return arr[x1][y1] - arr[x2-1][y1] - arr[x1][y2-1]  + arr[x2-1][y2-1]

def area(sx,sy,ex,ey):
    if ex == N-1 and ey == M-1:
        return 0
    max_value = 0
    if ex == N-1:
        for dy in range(ey+1,M-1):
            max_value = max(max_value, area_sum(ex,ey,sx,sy) * area_sum(ex,dy,0,ey+1) * area_sum(ex,M-1,0,dy+1))
        for dx in range(0,N-1):
            max_value = max(max_value,area_sum(ex,ey,sx,sy) * area_sum(dx,M-1,0,ey+1) * area_sum(N-1,M-1,dx+1,ey+1))
        return max_value
    elif ey == M-1:
        for dx in range(ex+1,N-1):
            max_value = max(max_value,area_sum(ex,ey,sx,sy) * area_sum(dx,ey,ex+1,0) * area_sum(N-1,ey,dx+1,0))
        for dy in range(0,M-1):
            max_value = max(max_value, area_sum(ex,ey,sx,sy) * area_sum(N-1,dy,ex+1,0) * area_sum(N-1,M-1 ,ex+1,dy+1))
        return max_value 
    else:
        max_value = max(area_sum(ex,ey,sx,sy) * area_sum(N-1,M-1,ex+1,0) * area_sum(ex,M-1,0,ey+1) , area_sum(ex,ey,sx,sy) * area_sum(N-1,M-1,0,ey+1) * area_sum(N-1,ey,ex+1,0))
        return max_value
    

N,M = map(int,input().split())


arr = [list(map(int,list(input())))+[0] for _ in range(N)]
arr.append([0 for _ in range(M+1)])


for i in range(N):
    for j in range(M):
        arr[i][j] = arr[i][j] + arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
result = 0
for i in range(N):
    for j in range(M):
        result = max(result,area(0,0,i,j),i,j)

print(result)