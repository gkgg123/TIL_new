# edenooo님 코드 복기
from itertools import permutations
def dfs(idx,cnt,position,num_list):
    global result
    if (cnt+N-1-idx)<Q:
        return
    if idx == N-1:
        position.append(idx)
        mul_val = 1
        sum_val = 0
        cu_idx = 0
        for mul_idx in position:
            while (cu_idx<=mul_idx):
                sum_val += num_list[cu_idx]
                cu_idx += 1
            mul_val *= sum_val
            sum_val = 0
        result = max(result,mul_val)
        position.pop()
        return
    dfs(idx+1,cnt,position,num_list)
    position.append(idx)
    if cnt+1<=Q:
        dfs(idx+1,cnt+1,position,num_list)
    position.pop()
N = int(input())
arr = list(map(int,input().split()))
result = 0
arr.sort()

P,Q = map(int,input().split())
for perm in permutations(arr):
    dfs(0,0,[],perm)
print(result)