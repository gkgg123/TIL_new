import sys
from math import gcd
def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    gaps = []
    for idx in range(N-1):
        if arr[idx+1] - arr[idx]:
            gaps.append(arr[idx+1]-arr[idx])

    if not gaps:
        print('INFINITY')
    else:
        answer = gaps[0]
        for num in gaps:
            answer = gcd(answer,num)
        print(answer)

