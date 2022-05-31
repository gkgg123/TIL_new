import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()



N,K = map(int,input().split())

arr = [0]+list(map(int,input().split()))
answer = 0
memoryed = defaultdict(int)
for i in range(N):
    arr[i+1] += arr[i]
    if arr[i+1] == K:
        answer += 1
    answer += memoryed[arr[i+1]-K]

    memoryed[arr[i+1]] += 1

print(answer)