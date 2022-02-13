N = int(input())
first_arr = list(map(int,input().split()))
idx_dict = {}
for idx in range(N):
    idx_dict[first_arr[idx]] = idx
second_arr = list(map(int,input().split()))
cnt = 0
for i in range(N):
    target_index = idx_dict[second_arr[i]]
    if target_index == i:
        continue
    idx_dict[second_arr[i]],idx_dict[first_arr[i]] = i,target_index
    first_arr[i],first_arr[target_index] = first_arr[target_index],first_arr[i]
    cnt += 1

if cnt%2:
    print('Impossible')
else:
    print('Possible')