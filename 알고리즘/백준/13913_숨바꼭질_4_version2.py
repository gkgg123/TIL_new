import sys
from collections import deque
input = sys.stdin.readline


N,M = map(int,input().split())

dp = [-1]*100001
stack = deque()
dp[N] = 0
root_list = [-1]*100001
stack.append((0,N))
if N > M:
    print(N-M)
    print(' '.join(map(str,range(N,M-1,-1))))
elif N == M:
    print(0)
    print(N)
else:
    flag = False
    while stack:
        cnt, x = stack.popleft()
        for ind,nx in enumerate([2*x,x-1,x+1]):
            if 0<=nx<100001:
                if dp[nx] == -1:
                    dp[nx] = cnt + 1
                    root_list[nx] = x
                    stack.append((cnt+1,nx))
                    if nx == M:
                        find_route = [nx]
                        cu_route = nx
                        while cu_route != N:
                            cu_route = root_list[cu_route]
                            find_route.append(cu_route)
                        flag = True
                        print(cnt+1)
                        print(*reversed(find_route))
                        break
        if flag:
            break

