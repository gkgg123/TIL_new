import sys

def input():
    return sys.stdin.readline()
def check(x,y):
    if x == 'i' and (y =='j' or y == 'l'):
        return True
    elif x == 'v' and y=='w':
        return True
    elif x == y:
        return True
    return False
N,M = map(int,input().split())

my_answer = [0]+list(input())
correct_answer = [0]+list(input())

# i => i,j,l
# v => v,w,
INF = float('inf')
dp = [[x if y==0 else y if x==0  else INF for y in range(M+1)] for x in range(N+1)]


for i in range(1,N+1):
    for j in range(1,M+1):
        if check(my_answer[i],correct_answer[j]):
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1

print(dp[N][M])