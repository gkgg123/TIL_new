import sys

def input():
    return sys.stdin.readline().rstrip()


M = int(input())
arr = list(input())
N = len(arr)
for le in range(M,0,-1):
    for c in range(N-le-1):
        print(arr[c] ,arr[c+le])
    print('--?')