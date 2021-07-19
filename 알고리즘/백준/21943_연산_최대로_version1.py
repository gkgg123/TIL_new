from itertools import combinations

def dfs(cu_val,cnt,pick_list):
    global result
    if cnt == 0:
        result = max(result,cu_val*sum(pick_list))
        return cu_val * sum(pick_list)
    else:

        idx_list = range(len(pick_list))
        for pick_cnt in range(1,len(pick_list)-cnt+1):
            for comb in combinations(idx_list,pick_cnt):
                copy_pick_list = pick_list[:]
                comb = list(reversed(comb))
                temp_sum = 0
                for idx in comb:
                    temp_sum += copy_pick_list.pop(idx)                
                dfs(cu_val*temp_sum,cnt-1,copy_pick_list)







N = int(input())

arr = list(map(int,input().split()))

p_cnt,a_cnt = map(int,input().split())


result = 0
dfs(1,a_cnt,arr)
print(result)