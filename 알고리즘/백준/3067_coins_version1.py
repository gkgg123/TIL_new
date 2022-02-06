import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int,input().split()))
    money = int(input())
    dp = [0 for _ in range(money+1)]
    dp[0] = 1

    for coin in coins:
        for k in range(money-coin+1):
            if k + coin <= money and dp[k]:
                dp[k+coin] += dp[k]

    print(dp[money])