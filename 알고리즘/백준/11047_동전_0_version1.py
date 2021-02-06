# 11047 동전_0

N,K = map(int,input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))
start = len(coins)-1
cnt = 0
while K > 0:
    if K - coins[start] >= 0:
        K -= coins[start]
        cnt += 1
    else:
        start -= 1


print(cnt)