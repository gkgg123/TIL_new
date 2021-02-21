import sys
input = sys.stdin.readline
def solution():
    global N
    for dep0 in range(N):
        for dep1 in graph[dep0]:
            for dep2 in graph[dep1]:
                if dep0 == dep2:
                    continue
                for dep3 in graph[dep2]:
                    if dep3 == dep1 or dep3 == dep0:
                        continue
                    for dep4 in graph[dep3]:
                        if dep4 != dep0 and dep4 != dep1 and dep4 != dep2:
                            return 1
    return 0

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(solution())