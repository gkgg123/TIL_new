import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()
def backtracking(idx,total):
    if idx == total:
        print(*visited)
        exit()
    elif visited[idx] == -1:
        for num in nums:
            if count[num] and visited[idx] == -1:
                if idx+num+1 <2*N and visited[idx+num+1] == -1:
                    visited[idx+num+1] = num
                    visited[idx] = num
                    count[num] -= 2
                    backtracking(idx+1,total)
                    visited[idx+num+1] = -1
                    visited[idx] = -1
                    count[num] += 2
    else:
        backtracking(idx+1,total)



N = int(input())
arr = list(map(int,input().split()))
visited = [-1 for _ in range(2*N)]
count = defaultdict(int)
total = 0
for num in arr:
    count[num] += 2
    total += 2
nums = sorted(count.keys())

backtracking(0,total)
print(-1)