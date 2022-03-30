from glob import glob
import sys

def input():
    return sys.stdin.readline().rstrip()


def gap(info,X):
    return True if max(info)-min(info) >= X else False

def sum_range(info):
    if L<=sum(info)<=R:
        return True
    return False
def dfs(idx,end,problems):
    if sum(problems) > R:
        return 0
    if idx == end:
        if sum_range(problems) and gap(problems,X) and len(problems)>=2:
            return 1
        else:
            return 0
    else:
        cnt = 0

        cnt += dfs(idx+1,end,problems+[arr[idx]])
        cnt += dfs(idx+1,end,problems)
        return cnt

N,L,R,X = map(int,input().split())


arr = list(map(int,input().split()))
answer = dfs(0,N,[])

print(answer)