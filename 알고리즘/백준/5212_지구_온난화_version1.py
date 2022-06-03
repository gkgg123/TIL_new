import sys

def input():
    return sys.stdin.readline().rstrip()


R,C = map(int,input().split())

arr = [list(input()) for _ in range(R)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
remove_area = []
for x in range(R):
    for y in range(C):
        if arr[x][y] == 'X':
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<R and 0<=ny<C:
                    if arr[nx][ny] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt>2:
                remove_area.append((x,y))

for x,y in remove_area:
    arr[x][y] = '.'

min_x = float('inf')
min_y = float('inf')
max_x = -1
max_y = -1
for x in range(R):
    for y in range(C):
        if arr[x][y] == 'X':
            min_x = min(min_x,x)
            min_y = min(min_y,y)
            max_x = max(max_x,x)
            max_y = max(max_y,y)
for x in range(min_x,max_x+1):
    print(''.join(arr[x][min_y:max_y+1]))
