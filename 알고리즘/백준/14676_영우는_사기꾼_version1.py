import sys
def input():
    return sys.stdin.readline().rstrip()

def solve():
    builded = [0 for _ in range(N+1)]
    for _ in range(K):
        command,num = map(int,input().split())
        if command == 1:
            if indegree[num]:
                return 'Lier!'
            if builded[num]:
                builded[num] += 1
                continue
            builded[num] += 1
            for child in graph[num]:
                indegree[child] -= 1   
        else:
            if not builded[num]:
                return 'Lier!'
            builded[num] -= 1
            if builded[num] == 0:
                for child in graph[num]:
                    indegree[child] += 1
    return 'King-God-Emperor'

N,M,K = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    indegree[y] += 1

print(solve())