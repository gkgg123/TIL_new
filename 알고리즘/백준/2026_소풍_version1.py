import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()

def checkFreinds(target_node,friend):

    for node in friend:
        if not friendly[node][target_node]:
            return False
    return True

def dfs(node,friend):
    global K,result
    if len(friend) == K:
        result = list(map(str,friend))
        sys.stdout.write('\n'.join(result))
        exit(0)
        return

    for next_node in range(node+1,N+1):
        if friend_cnt[next_node] < K-1:
            continue
        if visited[next_node]:
            continue
        if not friendly[node][next_node]:
            continue
        if not checkFreinds(next_node,friend):
            continue
        visited[next_node] = True
        dfs(next_node,friend +[next_node])
        visited[next_node] = False



K,N,F = map(int,input().split())

friendly = [[False for _ in range(N+1)] for _ in range(N+1)]

friend_cnt = [0 for _ in range(N+1)]
for _ in range(F):
    x,y = map(int,input().split())
    friendly[x][y] = True
    friendly[y][x] = True
    friend_cnt[x] += 1
    friend_cnt[y] += 1

result = []
visited = [False for _ in range(N+1)]
for num in range(1,N+1):
    if friend_cnt[num] < K-1:
        continue
    visited[num] = True
    dfs(num,[num])
    visited[num] = False

print(-1)