# 1309 동물원
# 9901로 나눈 수 출력

N = int(input())
mod = 9901
dp = [0]*(N+1)
if N == 1:
    print(3)
else:
    dp = [1,3]
    for i in range(2,N+1):
        current = 2*dp[-1]+dp[-2]
        dp[-2] = dp[-1]
        dp[-1] = current
    print(current%mod)