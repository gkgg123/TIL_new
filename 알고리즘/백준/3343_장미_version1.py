import sys
from math import lcm,ceil
def input():
    return sys.stdin.readline().rstrip()

# 가성비가 좋지 않은 곳은 최소공배수 이상 살일이 없다.
# 그러므로 가성비가 좋지 않은 곳에서 최소 공배수까지 완전탐색을 해서, 가성비가 좋지 않은것만큼 사고, 남은것을 가성비가 좋은걸 사면 된다.

N,AC,AP,BC,BP = map(int,input().split())
if AC*BP > BC*AP:
    AC,AP,BC,BP = BC,BP,AC,AP
LCM_count = lcm(BC,AC)
answer = float('inf')
A_COUNT = 0
while A_COUNT*AC < LCM_count:
    if N <= A_COUNT*AC:
        answer = min(answer,AP*A_COUNT)
        break

    B_Buy_TOTAL = N - AC*A_COUNT
    B_COUNT = ceil(B_Buy_TOTAL/BC)
    cost = A_COUNT*AP + B_COUNT*BP

    answer = min(answer,cost)

    A_COUNT += 1

print(answer)



