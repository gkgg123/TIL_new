import sys
sys.setrecursionlimit(100000)
def check(K):
    dp = [False for _ in range(N)]
    dp[0] = True
    for i in range(N-1):
        if dp[i]:
            for j in range(i+1,N):
                tempK = (j-i)*(abs(arr[i]-arr[j])+1)
                if tempK <= K:
                    dp[j] = True

    return dp[N-1]

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

arr = list(map(int,input().split()))
left = 0
right = 1000000

while left+1<right:
    mid = (left+right)//2

    if check(mid):
        right = mid
    else:
        left = mid

print(right)
