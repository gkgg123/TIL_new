import sys
def input():
    return sys.stdin.readline().rstrip()
dp = [[0 for _ in range(1001)] for _ in range(51)]

for count in range(1,51):
    dp[count][0] = 0
    for y in range(1,1001):
        dp[count][y] = dp[count][y-1] + dp[count-1][y-1] + 1


def solve(c,h):
    temp = 1
    while dp[c][temp] < h:
        temp += 1
    return temp
P = int(input())
for row in range(1,10):
    print(dp[row][:100])
for _ in range(P):
    count,height = map(int,input().split())
    print(solve(count,height))