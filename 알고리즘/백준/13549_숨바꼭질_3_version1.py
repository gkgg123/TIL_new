# 13549 숨바꼭질 3
import collections
import sys

sys.stdin = open('1.txt','r')

for _ in range(1000):
    start,end = map(int,input().split())
    dp = [-1]*100001
    dp[start] = 0
    dq = collections.deque()
    dq.append((start,0))
    if start == end:
        print(0)
    else:
        while True:
            x,time = dq.popleft()
            nx = 2*x
            while 0<nx <=100000:
                if dp[nx] == -1:
                    dp[nx] = time
                    dq.append((nx,time))
                nx = 2*nx
        
            if dp[end] != -1:
                break
            for nx in [x+1,x-1]:
                if 0<=nx<=100000:
                    if dp[nx] == -1:
                        dp[nx] = time + 1
                        dq.append((nx,time+1))
        
        print(dp[end])