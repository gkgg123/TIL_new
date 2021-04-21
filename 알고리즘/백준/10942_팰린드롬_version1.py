import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

dp = [[ True  if i == j else False for j in range (N)]  for i in range(N)]
for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = True

for i in range(2,N):
    for j in range(N-i):
        if arr[j] == arr[j+i] and dp[j+1][j+i-1]:
            dp[j][j+i] = True

M = int(input())

for _ in range(M):
    x,y = map(int,input().split())
    if dp[x-1][y-1]:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')
