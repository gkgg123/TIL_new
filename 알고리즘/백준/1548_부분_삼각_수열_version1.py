import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

arr = list(map(int,input().split()))
arr.sort()
answer = N
if N>2:
    answer = 2
    for st in range(N-2):
        for end in range(N-1,st+1,-1):
            if arr[st] + arr[st+1]> arr[end]:
                answer = max(answer,end-st+1)
                break
print(answer)