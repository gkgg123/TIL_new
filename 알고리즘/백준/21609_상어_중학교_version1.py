import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()
def rotate(arr):
    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            new_arr[x][y] = arr[y][N-x-1]
    return new_arr

def press(arr):
    new_arr = [[float('inf') for _ in range(N)] for _ in range(N)]
    for y in range(N):
        index = N-1
        x = N-1
        while x>=0:
            if arr[x][y]>=0 and arr[x][y] != float('inf'):
                new_arr[index][y] = arr[x][y]
                index -= 1
            elif arr[x][y] == -1:
                new_arr[x][y] = arr[x][y]
                index = x -1
            x -= 1
    return new_arr

def remove(arr):
    for x,y in remove_block['remove_block']:
        arr[x][y] = float('inf')
    arr = press(arr)
    arr = rotate(arr)
    arr = press(arr)
    return arr
def check(arr):
    visited = [[False for _ in range(N)] for _ in range(N)]
    infos = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] > 0 and not visited[x][y] and arr[x][y] != float('inf'):
                visited[x][y] = True
                queue = deque()
                queue.append((x,y))
                block_group = {
                    'remove_block' : [(x,y)],
                    'row' : x,
                    'col' : y,
                    'cnt' : 1,
                    'rainbow_cnt' : 0,
                }
                while queue:
                    cx,cy = queue.popleft()

                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]
                        if 0<=nx<N and 0<=ny<N:
                            if arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                                visited[nx][ny] = True
                                if block_group['row'] > nx:
                                    block_group['row'] = nx
                                if block_group['col'] > ny:
                                    block_group['col'] = ny
                                block_group['remove_block'].append((nx,ny))
                                block_group['cnt'] += 1
                                queue.append((nx,ny))
                            elif not arr[nx][ny] and (nx,ny) not in block_group['remove_block']:
                                block_group['remove_block'].append((nx,ny))
                                block_group['cnt'] += 1
                                block_group['rainbow_cnt'] += 1
                                queue.append((nx,ny))
                if block_group['cnt'] >= 2:
                    infos.append(block_group)
    return  infos
N,M = map(int,input().split())


maze = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
answer = 0
while True:
    block_info = check(maze)
    if not block_info:
        break
    block_info.sort(key = lambda x : (-x['cnt'], -x['rainbow_cnt'], -x['row'] , -x['col']))
    remove_block = block_info[0]
    answer += remove_block['cnt']**2
    maze = remove(maze)
print(answer)