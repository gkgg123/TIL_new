import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    M,N = map(int,input().split())
    arr = []
    sange = []
    fire_set = set()
    visited = [[True]*M for _ in range(N)]
    for x in range(N):
        input_list = list(input().strip())
        for y in range(M):
            if input_list[y] == '*':
                fire_set.add((x,y))
            elif input_list[y] == '@':
                sange.append((x,y))
                visited[x][y] = False
                input_list[y] = '.'
        arr.append(input_list)
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    times = 0
    result = 'IMPOSSIBLE'
    flag = False
    while sange:
        new_sange = []
        new_fire = set()
        for fire in fire_set:
            for i in range(4):
                nx = fire[0] + dx[i]
                ny = fire[1] + dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if arr[nx][ny] == '.':
                        new_fire.add((nx,ny))
                        arr[nx][ny] = '*'
        for sa in sange:
            for i in range(4):
                nx = sa[0] + dx[i]
                ny = sa[1] + dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if visited[nx][ny] and arr[nx][ny] == '.':
                        new_sange.append((nx,ny))
                        visited[nx][ny] = False
                else:
                    result = times+1
                    flag = True
                    break
        if flag:
            break
        times += 1
        sange = new_sange[:]
        fire_set = new_fire

    print(result)
                

