from math import log2
import sys
sys.setrecursionlimit(100005)
def input():
    return sys.stdin.readline().rstrip()


def sol(l,w,h):
    l,w,h = sorted([l,w,h])
    if l == 0:
        return 0
    k = int(log2(l))

    cnt = 0
    for i in range(k,-1,-1):
        cnt += (8**i) * cube_cnt[i]
    if cnt <8**k:
        return -float('inf')
    x = 2**k
    y = min(cnt//(x**3),h//x)
    cnt = (x**3)*y
    total = 0
    while cnt>0:
        mn = min(cube_cnt[k],cnt//(8**k))
        cnt -= (8**k)*mn
        cube_cnt[k] -= mn
        total += mn
        k -= 1
    return sol(l,w,h-(x*y)) + sol(l-x,w,x*y) + sol(x,w-x,x*y) + total


L,W,H = map(int,input().split())

N = int(input())

cube_cnt = [0 for _ in range(21)]
for _ in range(N):
    x,y = map(int,input().split())
    cube_cnt[x] = y

answer = sol(L,W,H)

if answer <= 0:
    print(-1)
else:
    print(answer)

