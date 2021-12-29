import sys


def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = [0]+list(map(int,input().split()))
Q = int(input())
prefix_sum = [0 for _ in range(N+1)]

for i in range(1,N+1):
    if arr[i] < arr[i-1]:
        prefix_sum[i] += 1
    prefix_sum[i] += prefix_sum[i-1]

for _ in range(Q):
    l,r = map(int,input().split())
    k = prefix_sum[r] - prefix_sum[l] + 1

    if k == 2 and arr[r] >arr[l]:
        k = 3
    elif k > 2:
        k = 3

    sys.stdout.write(f'{k}\n')