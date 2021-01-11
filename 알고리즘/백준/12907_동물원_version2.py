total = [0]*41
n = int(input())
arr = list(map(int,input().split()))
for num in arr:
    total[num] += 1
prev_cnt = 2
flag = False
for cnt in total:
    if cnt > prev_cnt:
        flag = True
        break
    prev_cnt = cnt

if flag:
    print(0)
else:
    result = 2**(total.count(2) + (1 in total))
    print(result)