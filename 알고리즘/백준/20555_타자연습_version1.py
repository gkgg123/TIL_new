import sys

def input():
    return sys.stdin.readline().rstrip()
def sol(idx_list,remain_lens):
    if dp.get(idx_list) == None:
        if remain_lens == 0:
            dp[idx_list] = 0
            return 0
        for prefix in ['A','B','C','D']:
            copy_list = list(idx_list)
            cnt = 0
            for idx in range(N):
                if copy_list[idx] >= len(arr[idx]):
                    continue
                if arr[idx][copy_list[idx]] == prefix:
                    cnt += 1
                    copy_list[idx] += 1
            if cnt>0:
                temp = sol(tuple(copy_list),remain_lens-cnt) + 1
                if dp.get(idx_list) != None:
                    dp[idx_list] = min(dp[idx_list],temp)
                else:
                    dp[idx_list] = temp
    return dp[idx_list]
def backtracking(idx_list):
    if dp[idx_list] == 0:
        return
    cur = dp[idx_list]
    for prefix in ['A','B','C','D']:
        copy_list = list(idx_list)
        cnt = 0
        for idx in range(N):
            if copy_list[idx] >= len(arr[idx]):
                continue
            if arr[idx][copy_list[idx]] == prefix:
                cnt += 1
                copy_list[idx] += 1
        if cur == dp[tuple(copy_list)] + 1:
            print(prefix,end='')
            backtracking(tuple(copy_list))
            break

N = int(input())

arr = []
answer = 0
result = []
for _ in range(N):
    s = input()
    answer += len(s)
    arr.append(s)
dp = {}
sol(tuple([0]*N),answer)
backtracking(tuple([0]*N))