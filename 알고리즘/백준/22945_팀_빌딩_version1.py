import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int,input().split()))


left = 0
right = N-1
answer = 0
while left<=right:
    answer = max((right-left-1)*min(arr[left],arr[right]),answer)

    if arr[left]> arr[right]:
        right -= 1
    else:
        left += 1

print(answer)