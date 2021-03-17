import sys

sys.setrecursionlimit(1000)
def dfs(node,cnt):
    for next_node,val in enumerate(arr[node]):
        if val and visited[next_node] == 0:
            visited[next_node] = cnt
            dfs(next_node,cnt)





N = int(input())
M = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

tour_list = list(map(int,input().split()))

visited = [0]*N
cnt = 1
for i in range(N):
    if visited[i] == 0:
        visited[i] = cnt
        dfs(i,cnt)
        cnt += 1

result = 'YES'
init = visited[tour_list[0]-1]
for city in tour_list[1:]:
    if visited[city -1] != init:
        result = 'NO'
print(result)