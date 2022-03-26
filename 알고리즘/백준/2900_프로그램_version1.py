import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()

def sol(jump,cnt):
    idx = 0
    while idx<N:
        arr[idx] += cnt
        idx += jump


N,K = map(int,input().split())

jumps = Counter(map(int,input().split()))

arr = [0 for i in range(N)]

for key in jumps:
    sol(key,jumps[key])
Q = int(input())
prefix_sum = [0] + arr[:]

for idx in range(1,N+1):
    prefix_sum[idx] += prefix_sum[idx-1]
for _ in range(Q):
    L,R = map(int,input().split())

    answer = prefix_sum[R+1] - prefix_sum[L]
    print(answer)