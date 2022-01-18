import sys
import string
from collections import deque,defaultdict
def input():
    return sys.stdin.readline().rstrip()



def converting(keys):
    temp = 0
    for key in keys:
        temp += (1<<lower_case[key])
    return temp

def bfs(x,y):
    global keys,visited
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    result = 0
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    door_dict = defaultdict(list)
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx<N+2 and 0<=ny<M+2 and not visited[nx][ny] and arr[nx][ny] != '*':
                if arr[nx][ny] == '.':
                    queue.append((nx,ny))
                elif arr[nx][ny] == '$':
                    result += 1
                    queue.append((nx,ny))
                elif arr[nx][ny].islower():
                    if not keys & (1<<lower_case[arr[nx][ny]]):
                        keys = keys|(1<<lower_case[arr[nx][ny]])
                        if arr[nx][ny] in door_dict:
                            queue.extend(door_dict[arr[nx][ny]])
                    queue.append((nx,ny))
                        
                elif arr[nx][ny].isupper():
                    lower_alpha = arr[nx][ny].lower()
                    if keys & (1<<lower_case[lower_alpha]):
                        queue.append((nx,ny))
                    else:
                        door_dict[lower_alpha].append((nx,ny))
                visited[nx][ny] = True
    return result

    

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    lower_case = {key : ind for ind,key in enumerate(string.ascii_lowercase)}
    upper_case = {key : ind for ind,key in enumerate(string.ascii_uppercase)}
    arr = [['.' for _ in range(M+2)]]

    for _ in range(N):
        temp = ['.']+list(input()) + ['.']
        arr.append(temp)
    arr.append(['.' for _ in range(M+2)])

    input_list = []
    keys = input()

    if not keys.isdigit():
        keys = converting(keys)
    else:
        keys = int(keys)
    

    visited = [[False for _ in range(M+2)] for _ in range(N+2)]

    print(bfs(0,0))

