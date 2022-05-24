import sys
from collections import defaultdict
from math import gcd
def input():
    return sys.stdin.readline().rstrip()

def solve(mid):
    cnt = defaultdict(int)
    for idx in range(N):
        if idx == mid:
            continue
        gx,gy = position[idx][0] - position[mid][0], position[idx][1] - position[mid][1]
        gcds = gcd(gx,gy)
        gx,gy = gx//gcds,gy//gcds

        cnt[(gx,gy)] += 1
    total = 0
    for gx,gy in cnt:
        if cnt.get((-gy,gx)):
            total = total + cnt[(gx,gy)] * cnt[(-gy,gx)]

    return total


N = int(input())

position = []
for _ in range(N):
    x,y = map(int,input().split())
    position.append((x,y))



answer = 0

for i in range(N):
    answer += solve(i)

print(answer)