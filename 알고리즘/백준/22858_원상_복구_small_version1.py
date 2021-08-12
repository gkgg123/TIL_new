import sys

def input():
    return sys.stdin.readline().rstrip()

N,K = map(int,input().split())
arr = list(map(int,input().split()))
D = list(map(int,input().split()))

while K:
    
    new_arr = [0 for _ in range(N)]
    for ind, prev_ind in enumerate(D):
        new_arr[prev_ind-1] = arr[ind]
    K -= 1
    arr = new_arr[:]
print(*arr)