import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()


N,B,W = map(int,input().split())
stons = input()
left = 0
right = 0
cnt = defaultdict(int)
answer = 0
while right<N:
    cnt[stons[right]] += 1
    if cnt['W'] >= W and cnt['B'] <=B:
        answer = max(answer,right-left+1)

    while left<=right and cnt['B'] >B:
        cnt[stons[left]] -= 1
        left += 1
    right += 1

print(answer)
    