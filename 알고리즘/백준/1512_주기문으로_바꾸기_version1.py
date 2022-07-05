import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()


M = int(input())
arr = list(input())
N = len(arr)
answer = float('inf')
for le in range(M,0,-1):
    check = [defaultdict(int) for _ in range(le)]
    for c in range(N):
        check[c%le][arr[c]] += 1
    cnt = 0
    for i in range(le):
        cnt = cnt + sum(check[i].values()) - max(check[i].values())
    answer = min(answer,cnt)
print(answer)
        