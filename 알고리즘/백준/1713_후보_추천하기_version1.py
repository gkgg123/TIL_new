import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
K = int(input())

command = list(map(int,input().split()))
sajin = []
recommend = defaultdict(int)

for co in command:
    if co in sajin:
        recommend[co] += 1
    elif len(sajin) < N:
        sajin.append(co)
        recommend[co] += 1
    else:
        min_val = float('inf')
        min_idx = -1
        for idx in range(N):
            num = sajin[idx]
            if recommend[num] < min_val:
                min_val = recommend[num]
                min_idx = idx
        del recommend[sajin[min_idx]]
        sajin.pop(min_idx)
        sajin.append(co)
        recommend[co] += 1
sajin.sort()
print(*sajin)