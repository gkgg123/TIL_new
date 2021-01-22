# 입력 지폐의 금액 T 동전의 가지수 k 각 동전 하나의 금액 pi ni가 주어진다.
# 방법의 수는 2^31 -1 을 초과하지 않는다.



T = int(input())

k = int(input())

money = [list(map(int,input().split())) for _ in range(k)]

money.sort(reverse=True)
dp = (T+1)*[0]

dp[0] = 1
for coin_val,coin_cnt in money:
    for current_money in range(T,1,-1):
        for current_cnt in range(1,coin_cnt+1):
            if current_money - current_cnt*coin_val >= 0:
                dp[current_money] += dp[current_money-current_cnt*coin_val]
            else:
                break
print(dp[T])