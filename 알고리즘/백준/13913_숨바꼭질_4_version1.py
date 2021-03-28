import sys
import heapq
input = sys.stdin.readline


N,M = map(int,input().split())

dp = [-1]*100001
stack = []
dp[N] = 0
root_dict = {}
root_dict[N] = -1
heapq.heappush(stack,(0,N))
if N == M:
    print(0)
    print(N)
else:
    flag = False
    while stack:
        cnt, x = heapq.heappop(stack)
        for ind,nx in enumerate([2*x,x-1,x+1]):
            if 0<=nx<100001:
                if dp[nx] == -1:
                    dp[nx] = cnt + 1
                    root_dict[nx] = x
                    heapq.heappush(stack,(cnt+1,nx))
                    if nx == M:
                        find_route = [nx]
                        cu_route = nx
                        while cu_route != N:
                            cu_route = root_dict[cu_route]
                            find_route.append(cu_route)
                        flag = True
                        print(cnt+1)
                        print(*reversed(find_route))
                        break
        if flag:
            break

