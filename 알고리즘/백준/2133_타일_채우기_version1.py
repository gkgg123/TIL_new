# 2133 타일 채우기

#  3*N 크기의 벽을 2*1 1*2로 채우는 경우의 수를 구해보자
# N = 1 => 0
# N = 2 => 3
# N = 3 => 0
N= int(input())
dp = [0]*31
dp[2] = 3
if N%2:
    print(0)
else:
    # 점화식
    # Dp(N) = DP(N-2)*3 + (2*Dp(N-4)+2*DP(N-6)+2*DP(2))
    for number in range(4,N+2,2):
        temp = 2
        for k in range(number-4,0,-2):
            temp += dp[k]*2
        temp += dp[number-2]*3
        dp[number] = temp
    print(dp[N])
