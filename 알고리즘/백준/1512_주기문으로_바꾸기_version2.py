import sys
def input():
    return sys.stdin.readline().rstrip()
M = int(input())
arr = input()
N = len(arr)
answer = float('inf')
pick = {'A':0,'G':1,'C':2,'T':3}
for period in range(1,M+1):
    cnt = 0
    for idx in range(period):
        period_idx = [0]*4
        for pick_idx in range(idx,N,period):
            period_idx[pick[arr[pick_idx]]] += 1
        cnt = cnt + sum(period_idx) - max(period_idx)
    answer = min(answer,cnt)
print(answer)
