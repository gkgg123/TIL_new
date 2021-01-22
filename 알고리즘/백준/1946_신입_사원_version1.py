import sys

T = int(input())

for tc in range(T):
    N = int(input())
    result = 0
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    arr.sort()
    min_value = arr[0][1]
    for ind in range(N):
        if ind == 0:
            result += 1
        else:
            if min_value > arr[ind][1]:
                min_value = arr[ind][1]
                result += 1
    print(result)