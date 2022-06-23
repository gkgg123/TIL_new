import sys
from collections import deque
def bfs(arr):
    end = ''.join(sorted(arr))
    queue = deque()
    if ''.join(arr) == end:
        return 0
    queue.append((''.join(arr),0))
    visit = set()
    visit.add(''.join(arr))
    while queue:
        cur, cnt = queue.popleft()
        for idx in range(N-K+1):
            next_val = cur[:idx] + cur[idx:idx+K][::-1] + cur[idx+K:]
            if next_val not in visit:
                visit.add(next_val)
                queue.append((next_val,cnt+1))
                if next_val == end:
                    return cnt+1
    return -1

def input():
    return sys.stdin.readline().rstrip()

N,K = map(int,input().split())

    
arr = list(input().split())


print(bfs(arr))