import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    max_value = arr[-1]
    answer = 0
    for ind in range(N-2,-1,-1):
        if arr[ind] > max_value:
            max_value = arr[ind]
        else:
            answer = answer + max_value - arr[ind]
    print(answer)