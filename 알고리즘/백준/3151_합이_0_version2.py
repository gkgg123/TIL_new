import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int,input().split()))

mid = 20000
cnt = [0 for _ in range(40001)]
result = 0
for i in range(N):
    result += cnt[mid-arr[i]]
    for j in range(i):
        cnt[mid+arr[i]+arr[j]] += 1
print(result) 