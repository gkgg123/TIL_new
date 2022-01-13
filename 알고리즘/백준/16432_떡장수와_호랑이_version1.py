import sys

def input():
    return sys.stdin.readline()


def dfs(days,dd):
    if days == N:
        for d in dd:
            print(d)
        exit()
    else:
        for s in dduck[days]:
            if s != dd[-1] and visited[days][s]:
                visited[days][s] = False
                dfs(days+1,dd+[s])


N = int(input())


visited = [[True for _ in range(10)] for _ in range(N)]


dduck = []

for _ in range(N):
    count,*temp = map(int,input().split())
    dduck.append(temp)

for s in dduck[0]:
    visited[0][s] = False
    dfs(1,[s])
print(-1)