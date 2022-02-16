import sys

def input():
    return sys.stdin.readline().rstrip()



while True:

    N,M = map(float,input().split())

    M = int(M*100+0.5)
    arr = []
    if N+M == 0:
        break
    for _ in range(int(N)):
        x,y = map(float,input().split())
        arr.append((int(y*100+0.5),int(x)))


    dp = [-1 for _ in range(M+1)]
    dp[0] = 0


    arr.sort()


    for coin,cal in arr:

        for prev in range(M-coin+1):

            if dp[prev] != -1:
                dp[prev+coin] = max(dp[prev+coin],dp[prev] + cal)



    print(dp[M])