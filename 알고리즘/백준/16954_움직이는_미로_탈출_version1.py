import sys



input =sys.stdin.readline

def wall_move(origin_list):
    temp = []

    for x,y in origin_list:
        if x == 7:
            continue
        else:
            arr[x][y] = '.'
            temp.append((x+1,y))
    for x,y in temp:
        arr[x][y] = '#'
    return temp



arr = []
wall = []
for x in range(8):
    input_list = list(input().strip())
    for y in range(8):
        if input_list[y] == '#':
            wall.append((x,y))
    arr.append(input_list)

start = (7,0)

stack = []
stack.append(start)
result = 0
times = 0
dx = [-1,0,1,-1,0,1,-1,0,1]
dy = [-1,-1,-1,0,0,0,1,1,1]
while stack:
    visited = [[True]* 8 for _ in range(8)]
    new_stack = []

    for x,y in stack:
        if arr[x][y] == '#':
            continue
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<8 and 0<=ny<8 and arr[nx][ny] == '.' and visited[nx][ny]:
                new_stack.append((nx,ny))
                visited[nx][ny] = False
    
    if (0,7) in new_stack:
        result = 1
        break


    wall = wall_move(wall)

    stack = new_stack[:]

print(result)