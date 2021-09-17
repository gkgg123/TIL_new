import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    coins = []
    total_coins = 0
    for _ in range(N):
        a,b = map(int,input().split())
        coins.append((a,b))
        total_coins += a*b
    if total_coins%2:
        return 0
    else:
        find_coin = total_coins//2
        dp = [0 for _ in range(find_coin+1)]
        dp[0] = 1
        coins.sort(key= lambda x : -x[1])
        acc_coins = 0
        for coin,cnts in coins:
            max_coin = coin*cnts
            for i in range(min(max(acc_coins,max_coin),find_coin),coin-1,-1):
                if dp[i-coin]:
                    for cnt in range(cnts):
                        next_coin = coin*cnt + i
                        if 0<=next_coin<=find_coin:
                            dp[next_coin] = 1
            if dp[find_coin]:
                return 1
            acc_coins += max_coin
        return 0
for _ in range(3):
    print(solution())
    

