import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()
def check(cur):
    num_idx = defaultdict(list)

    for idx,num in enumerate(cur):
        num_idx[num].append(idx)
    
    for num in num_idx:
        if len(num_idx[num]) == 2:
            one,two = num_idx[num]
            if two - one!= num +1:
                return False
    return True
def backtracking(idx,total,cur):
    if not check(cur):
        return
    if idx == total:
        print(*cur)
        exit()
    else:
        for num in nums:
            if count[num]:
                count[num] -= 1
                backtracking(idx+1,total,cur+[num])
                count[num] += 1


N = int(input())
arr = list(map(int,input().split()))

count = defaultdict(int)
total = 0
for num in arr:
    count[num] += 2
    total += 2
nums = sorted(count.keys())
max_num = max(nums)
if 2*N-1 <max_num:
    print(-1)
else:
    backtracking(0,total,[])
    print(-1)