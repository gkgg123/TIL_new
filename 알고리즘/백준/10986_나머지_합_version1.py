import sys

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())


arr = [0] + list(map(int,input().split()))

cnt = [0 for i in range(M+1)]

for idx in range(1,N+1):
    arr[idx] += arr[idx-1]
    arr[idx] %= M

    cnt[arr[idx]] += 1

result = cnt[0]

for num in range(M):
    num_cnt = cnt[num]
    result = result + (num_cnt-1)*num_cnt//2

print(result)