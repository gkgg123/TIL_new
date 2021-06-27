from collections import defaultdict

N = int(input())

arr = list(input())

cnt_dict = defaultdict(int)
result = 0
prev_idx = -1
for idx in range(N):
    alpha = arr[idx]
    cnt_dict[alpha] = idx
    if len(cnt_dict) > N:
        min_idx = 100001
        min_key = -1
        for key in cnt_dict:
            if min_idx > cnt_dict[key]:
                min_idx = cnt_dict[key]
                min_key = key
        prev_idx = min_idx
        del cnt_dict[min_key]
    
    result = max(result,idx-prev_idx)
print(result)
