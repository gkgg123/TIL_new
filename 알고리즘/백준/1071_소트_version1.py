N = int(input())
arr = list(map(int,input().split()))

num_cnt = [0]*1005

for num in arr:
    num_cnt[num] += 1


cur = 0
result = []
while sum(num_cnt)>0:
    if num_cnt[cur]:
        if num_cnt[cur+1]:
            for next_num in range(cur+2,1001):
                if num_cnt[next_num]:
                    result.extend(num_cnt[cur]*[cur])
                    result.append(next_num)
                    num_cnt[cur] = 0
                    num_cnt[next_num] -= 1
                    break
            else:
                result.extend(num_cnt[cur+1]*[cur+1])
                result.extend(num_cnt[cur]*[cur])
                num_cnt[cur] = 0
                num_cnt[cur+1] = 0

        else:
            while num_cnt[cur]:
                result.append(cur)
                num_cnt[cur] -= 1
    cur += 1

print(*result)

