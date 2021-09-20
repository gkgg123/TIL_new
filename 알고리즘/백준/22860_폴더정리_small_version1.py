from collections import defaultdict,Counter
import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(position):
    temp = Counter(files[position])

    for next_folder in folders[position]:
        temp += dfs(next_folder)
    result[position] = [len(temp),sum(temp.values())]
    return temp
    

N,M = map(int,input().split())

folders = defaultdict(list)
files = defaultdict(set)
for _ in range(N+M):
    upper,lower,isFolder = input().split()
    if isFolder == '1':
        folders[upper].append(lower)
    else:
        files[upper].add(lower)

result = {}
dfs('main')


Q = int(input())
for _ in range(Q):
    last_folder = input().split('/')[-1]
    print(*result[last_folder])