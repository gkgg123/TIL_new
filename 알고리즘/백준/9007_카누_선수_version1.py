import sys
from bisect import bisect_left
def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    k,n = map(int,input().split())

    weights = [list(map(int,input().split())) for _ in range(4)]

    a = set()
    b = set()

    for i in range(n):
        for j in range(n):
            a.add(weights[0][i] + weights[1][j])
            b.add(weights[2][i] + weights[3][j])

    a = list(a)
    a.sort()
    b = list(b)
    b.sort()

    answer = float('inf')
    diff = float('inf')

    i = 0
    j = len(b)-1
    while i < len(a) and j >=0:
        if abs(a[i] + b[j] -k) <diff:
            diff = abs(a[i] + b[j] -k)
            answer = a[i] + b[j]
        elif abs(a[i] +b[j] - k) == diff:
            answer = min(answer,a[i] + b[j])
        if a[i] + b[j] > k:
            j -= 1
        elif a[i] + b[j] <k:
            i += 1
        else:
            break

    print(answer)