from collections import deque
def func(x):
    return x[0]
T = int(input())

for _ in range(T):
    N,M = map(int,input().split())

    arr = list(map(int,input().split()))
    queue = deque()
    for ind,val in enumerate(arr):
        queue.append((val,ind))

    cnt = 0
    while queue:
        val, ind = queue.popleft()
        if not queue or val >= max(queue,key=func)[0]:
            cnt += 1
            if ind == M:
                break
        else:
            queue.append((val,ind))

    print(cnt)
