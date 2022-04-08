import sys


def input():
    return sys.stdin.readline().rstrip()

def dfs(idx,end_idx):
    if idx == end_idx:
        return 1
    if currents[idx] != -1:
        return dfs(idx+1,end_idx)
    cnt = 0
    for num in range(1,N+1):
        if counts[num]:
            next_idx = idx + num + 1
            if next_idx >= 2*N:
                continue
            if currents[next_idx] == -1:
                currents[idx] = num
                currents[next_idx] = num
                counts[num] -= 2
                cnt += dfs(idx+1,end_idx)
                currents[idx] = -1
                currents[next_idx] = -1
                counts[num] += 2
    return cnt

N,X,Y = map(int,input().split())
X -= 1
Y -= 1
gab = max(X,Y) - min(X,Y)-1
counts = [2 for _ in range(N+1)]
counts[gab] = 0
currents = [-1 for _ in range(2*N)]

currents[X] = gab
currents[Y] = gab


print(dfs(0,2*N))