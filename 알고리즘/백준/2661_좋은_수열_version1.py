import sys

def input():
    return sys.stdin.readline().rstrip()


def check(st):
    n = len(st)

    for repeat_n in range(1,n//2+1):
        if st[n-2*repeat_n:n-repeat_n] == st[n-repeat_n:]:
            return False
    return True

def dfs(idx,stack):
    if idx == N:
        print(''.join(stack))
        exit()
    else:
        for i in ['1','2','3']:
            if check(stack+[i]):
                dfs(idx+1,stack+[i])
                


N = int(input())


dfs(1,['1'])