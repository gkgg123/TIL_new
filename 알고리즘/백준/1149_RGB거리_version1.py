# 1149번 RGB 거리

#  RGB 거리엔 N개의 집 1~N 순서대로
# 빨 초 파 중 하나
# 비용의 최소값 구하기
# 1번집의 색 != 2번집의 색
# N번집의 색은 N-1 번집의 색과 같지 않아야한다.

N = int(input())
# RGB
arr = [list(map(int,input().split())) for _ in range(N)]
INF = float('inf')
dp = [[INF] *3  for _ in range(N)]
for i in range(3):
    dp[0][i] = arr[0][i]

for x in range(1,N):
    for y in range(3):
        for z in range(3):
            if y != z:
                dp[x][y] = min(dp[x][y],dp[x-1][z]+arr[x][y])
print(min(dp[N-1]))