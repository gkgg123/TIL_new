import sys

def input():
    return sys.stdin.readline().rstrip()

def check(num,N):
    return (num+1)*(N-num+1)
def solve(N,K):
    left = -1
    right = N//2+1
    while left+1<right:
        mid = (left+right)//2
        ans = check(mid,N)
        if ans == K:
            return 'YES'
        elif ans>K:
            right = mid
        else:
            left = mid

    return 'NO'
    
    

N,K = map(int,input().split())


print(solve(N,K))