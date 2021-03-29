import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

if N == 1:
    print(-1)
else:
    total_sum = sum(arr)
    dp = [[-1] * total_sum for _ in range(N)]
    dp[0][0] = 0
    dp[0][arr[0]] = arr[0]
    for ind in range(N-1):
        for j in range(total_sum//2+1):
            if dp[ind][j] != -1:
                # 다음 거의 블록을 쓰지 않을때
                dp[ind+1][j] = max(dp[ind][j],dp[ind+1][j])
                # 두 탑 중 더 높은 탑쪽에 블록을 쌓을때
                if j + arr[ind+1] < total_sum:
                    dp[ind+1][j+arr[ind+1]] = max(dp[ind+1][j+arr[ind+1]],dp[ind][j]+arr[ind+1])
                # 더 낮은 탑 쪽에 쌓는데 새로 쌓는 블록이 기존 블록보다 높을때 와 아닐때
                if arr[ind+1] > j:
                    dp[ind+1][arr[ind+1]-j] = max(dp[ind+1][arr[ind+1]-j],dp[ind][j] + arr[ind+1]-j)
                else:
                    dp[ind+1][j-arr[ind+1]] = max(dp[ind+1][j-arr[ind+1]],dp[ind][j])
    if dp[-1][0] == 0:
        print(-1)
    else:
        print(dp[-1][0])
