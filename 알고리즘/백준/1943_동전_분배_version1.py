import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

max_coins = 50000
for _ in range(3):
    N = int(input())
    coins = defaultdict(int)
    dp = [0 for _ in range(max_coins+1)]
    dp[0] = 1
    total_sum = 0
    for _ in range(N):
        coin,cnts = map(int,input().split())
        for cur_coin in range(max_coins,coin-1,-1):
            if dp[cur_coin - coin]:
                for cnt in range(cnts):
                    next_coin = cur_coin + coin * cnt
                    if 0<=next_coin<=max_coins:
                        dp[next_coin] = 1
        total_sum += coin*cnts

    if total_sum%2 or not dp[total_sum//2]:
        print(0)
    else:
        print(1)



    