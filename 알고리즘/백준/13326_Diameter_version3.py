# Koosaga
import sys

def input():
    return sys.stdin.readline().rstrip()

def distance(p1,p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return x*x + y*y
N = int(input())
arr = []

for _ in range(N):
    x,y = map(int,input().split())
    arr.append([x,y])

st = 0
cur = -1

for i in range(N):
    for j in range(i):
        nxt = distance(arr[i],arr[j])
        if nxt > cur:
            cur = nxt
            st = i


arr[0],arr[st] = arr[st],arr[0]
stan_point = arr[0]
arr.sort(key= lambda p : distance(stan_point,p))
prefix_sum = [0 for _ in range(N+1)]
suffix_sum = [0 for _ in range(N+1)]
for i in range(N):
    for j in range(i):
        prefix_sum[i] = max(prefix_sum[i],distance(arr[i],arr[j]))
    for j in range(i+1,N):
        suffix_sum[i] = max(suffix_sum[i],distance(arr[i],arr[j]))


for i in range(1,N):
    prefix_sum[i] = max(prefix_sum[i],prefix_sum[i-1])
    suffix_sum[N-1-i] = max(suffix_sum[N-1-i],suffix_sum[N-i])

answer = float('inf')

for i in range(N-1):
    answer = min(answer,prefix_sum[i]**0.5 + suffix_sum[i+1]**0.5)
print(answer)