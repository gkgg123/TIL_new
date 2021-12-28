import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = [input() for _ in range(N)]

new_arr = [[False for _ in range(N)] for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for x in range(N):
    for y in range(N):
        if arr[x][y] == '.':
            continue
        if arr[x][y] == 'O':
            stack = [(x,y)]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                while  0<=nx<N and 0<=ny<N and arr[nx][ny] == '.':
                    new_arr[nx][ny] = True
                    nx += dx[i]
                    ny += dy[i]


for x in range(N):
    for y in range(N):
        if new_arr[x][y]:
            new_arr[x][y] = '.'
        elif arr[x][y] == '.':
            new_arr[x][y] = 'B'
        else:
            new_arr[x][y] = arr[x][y]

for row in new_arr:
    print(''.join(row))
