import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    d,n = map(int,input().split())

    mod = [ 0 for _ in range(d)]
    arr = list(map(int,input().split()))
    prefix_sum = [0] + arr[:]

    for i in range(n):
        prefix_sum[i+1] += prefix_sum[i]
        prefix_sum[i+1] %= d
        mod[prefix_sum[i+1]] += 1

    result = mod[0]

    for i in range(d):
        result += (mod[i] * (mod[i]-1))//2

    print(result)