import sys

from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()
N = int(input())

dp = [[defaultdict(int) for _ in range(10)] for _ in range(N+1)]


if N == 1:
    print(0)
else:
    for num in range(10):
        dp[1][num][1<<num] = 1


    for jari in range(2,N+1):
        for prev in range(10):
            for cur in [prev-1,prev+1]:
                if cur<0 or cur>9:
                    continue
                for prev_state in dp[jari-1][prev]:
                    cur_state = prev_state|(1<<cur)
                    dp[jari][cur][cur_state] += dp[jari-1][prev][prev_state]
                    dp[jari][cur][cur_state] = dp[jari][cur][cur_state]% 1000000000

    answer = 0
    for i in range(1,10):
        answer += dp[N][i][(1<<10)-1]
    print(answer% 1000000000)