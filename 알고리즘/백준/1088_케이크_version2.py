import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int,input().split()))
cnt = [1 for _ in range(N)]

answer = max(arr) - min(arr)
M = int(input())
while M:
    max_val = 0 
    max_idx = -1
    if not answer:
        break
    for i in range(N):
        if arr[i] > max_val:
            max_idx = i
            max_val = arr[i]
        elif arr[i] == max_val and cnt[max_idx] > cnt[i]:
            max_idx = i

    origin = arr[max_idx] * cnt[max_idx]
    cnt[max_idx] += 1
    now = origin/cnt[max_idx]
    arr[max_idx] = now
    answer = min(answer,max(arr)-min(arr))
    M -= 1
    print(arr)
print(f'{answer:.16f}')