import sys

def check(idx,cnt):
    global result
    if idx == N:
        result = max(result,cnt)
        print(result)
        exit()
        return
    else:
        for next_idx in range(idx+1,N,2):
            if dp[idx][next_idx]:
                check(next_idx+1,cnt+1)
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

dp = [[ True  if i == j else False for j in range (N)]  for i in range(N)]
for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = True

for i in range(2,N):
    for j in range(N-i):
        if arr[j] == arr[j+i] and dp[j+1][j+i-1]:
            dp[j][j+i] = True

max_num = N//2
result = -1
check(0,0)
print(result)