N, M  = map(int,input().split())
not_visited_days = [True]*(N+1)
if M:
    for k in list(map(int,input().split())):
        not_visited_days[k] = False
        

INF = float('inf')
dp = [[INF for _ in range(40)] for _ in range(105)] 

dp[0][0] = 0


for day in range(N):
    for coupon in range(37):
        if not not_visited_days[day+1]:
            dp[day+1][coupon] = min(dp[day+1][coupon],dp[day][coupon])
        dp[day+1][coupon] = min(dp[day+1][coupon],dp[day][coupon] + 10000)
        dp[day+3][coupon+1] = min(dp[day+3][coupon+1],dp[day][coupon] + 25000)
        dp[day+5][coupon+2] = min(dp[day+5][coupon+2],dp[day][coupon] + 37000)

    for coupon in range(39,2,-1):
        dp[day+1][coupon-3] = min(dp[day+1][coupon-3],dp[day][coupon])
    

print(min(dp[N]))
    
    
    

