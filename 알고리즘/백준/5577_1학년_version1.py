N = int(input())

arr = list(map(int,input().split()))
dp = [[0]*21 for _ in range(N)]

dp[0][arr[0]] = 1
for ind in range(1,N-1):
    for prev_num in range(21):
        if dp[ind-1][prev_num]:
            for new_num in [prev_num+arr[ind],prev_num-arr[ind]]:
                if 0<=new_num<=20:
                    dp[ind][new_num] += dp[ind-1][prev_num]

print(dp[N-2][arr[-1]])