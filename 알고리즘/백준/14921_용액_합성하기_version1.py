import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())


arr = list(map(int,input().split()))

arr.sort()
left = 0

right = N-1
result = float('inf')
while left<right:
    f = arr[left] + arr[right]
    if abs(f)<abs(result):
        result = f
    if f <0:
        left += 1
    else:
        right -= 1


print(result)