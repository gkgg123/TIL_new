import sys
from collections import deque
input = sys.stdin.readline

def bfs(stack):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while stack:
        x,y = stack.popleft()
        flag = visited[x][y] if visited[x][y] != 'FIRE' else 'FIRE'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == -1 and (arr[nx][ny] == '.' or arr[nx][ny] == '@'):
                    if flag == 'FIRE':
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    stack.append((nx,ny))
            else:
                if flag != 'FIRE':
                    return flag + 1
    return 'IMPOSSIBLE'





for _ in range(int(input())):
    M,N = map(int,input().split())
    stack = deque()
    arr = []
    visited = [[-1]*M for _ in range(N)]
    for x in range(N):
        input_list = input()
        for y in range(M):
            if input_list[y] == '*':
                stack.append((x,y))
                visited[x][y] = 'FIRE'
            elif input_list[y] == '@':
                start = (x,y)
                visited[x][y] = 0
        arr.append(input_list)
    stack.append(start)
    print(bfs(stack))
