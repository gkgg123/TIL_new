import heapq
start,end = map(int,input().split())
dp = [-1]*100001
dp[start] = 0

stack = []
heapq.heappush(stack,(0,start))
if start == end:
    print(0)
else:
    while stack:
        time,x = heapq.heappop(stack)
        for ind,nx in enumerate([2*x,x+1,x-1]):
            if 0<=nx<100001:
                if dp[nx] == -1:
                    if ind == 0:
                        dp[nx] = time
                        heapq.heappush(stack,(time,nx))
                    else:
                        dp[nx] = time +1
                        heapq.heappush(stack,(time+1,nx))
        if dp[end] != -1:
            print(dp[end])
            break
