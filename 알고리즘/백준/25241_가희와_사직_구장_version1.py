import sys
from itertools import permutations
def input():
    return sys.stdin.readline().rstrip()
def pick(po):
    return arr[po//C][po%C]
def isAlmost(po1,po2):
    x1,y1 = po1//C,po1%C
    x2,y2 = po2//C,po2%C
    if abs(x1-x2) + abs(y1-y2) == 1:
        return 1
    if abs(x1-x2) == 1 and abs(y1-y2) == 1:
        return 1
    return 0
    
R,C,N = map(int,input().split())

three = list(map(int,input().split()))
special = list(map(int,input().split()))

arr = [list(map(int,input().split())) for _ in range(R)]

max_sort = []
for x in range(R):
    for y in range(C):
        max_sort.append((arr[x][y],x*C+y))
max_sort.sort(key = lambda x : (-x[0],x[1]))
top_N = 0
top_visit = set()
visits = []
ans = 0
for val,position in max_sort:
    if len(top_visit) <N:
        top_visit.add(position)
        top_N += val
        visits.append((val,position))
    else:
        break
special.sort(reverse=True)
for a in range(R*C-2):
    for b in range(a+1,R*C-1):
        for c in range(b+1,R*C):
            temp = sum(special[:isAlmost(a,b) +isAlmost(b,c) + isAlmost(a,c)])
            outofRange = 0
            for num in [a,b,c]:
                if num not in top_visit:
                    outofRange += 1
                    temp += pick(num)

            copy_top_N = top_N
            idx = N-1
            while outofRange:
                cur_val, cur_position = visits[idx]
                idx -= 1
                if cur_position in [a,b,c]:
                    continue
                copy_top_N -= cur_val
                outofRange -= 1
            temp += copy_top_N
            if temp > ans:
                ans = temp
        
print(ans)