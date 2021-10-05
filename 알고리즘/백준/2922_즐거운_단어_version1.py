import sys
from functools import lru_cache
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()

def continuity(w):
    if w[-1] == w[-2] == w[-3]:
        return True
    return False
@lru_cache()
def dfs(idx,words,a_cnt,b_cnt):
    global N
    cnt = 0
    if idx == N:
        if continuity(words):
            return 0
        if not (flag or b_cnt):
            return 0
        if flag:
            return 21**(b_cnt)*5**(a_cnt)
        else:
            return (21**(b_cnt) - 20**(b_cnt))*5**(a_cnt)
    if idx >=3 and continuity(words):
        return 0
    if arr[idx] == '_':
        cnt += dfs(idx+1,(*words,'A'),a_cnt+1,b_cnt)
        cnt += dfs(idx+1,(*words,'B'),a_cnt,b_cnt+1)
    elif arr[idx] in 'AEIOU':
        cnt += dfs(idx+1,(*words,'A'),a_cnt,b_cnt)
    else:
        cnt += dfs(idx+1,(*words,'B'),a_cnt,b_cnt)
    return cnt


arr = list(input())

N = len(arr)
flag = False
if arr.count('L'):
    flag = True

print(dfs(0,(),0,0))