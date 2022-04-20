
def compression(line):
    temp = []
    for x in line:
        if x == 0:
            continue
        temp.append(x)
    new_line = [0 for _ in range(N)]
    if temp:
        index = 0
        for val in temp:
            if new_line[index] == val:
                new_line[index] *= 2
                index += 1
            elif new_line[index]:
                index += 1
                new_line[index] = val
            else:
                new_line[index] = val
    return new_line

def rotate(maze):
    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            new_arr[x][y] = maze[y][N-x-1]
    return new_arr
def solve(idx,maze):
    global  answer
    if idx == 5:
        max_value = max(list(map(max,maze)))
        answer = max(answer,max_value)
        return

    for _ in range(4):
        new_arr = []
        for line in maze:
            new_arr.append(compression(line))
        solve(idx+1,new_arr)
        maze = rotate(maze)


dx = [-1,0,1,0]
dy = [0,-1,0,1]

N = int(input())
start_position = [(0,0,N,N,1,1),(N-1,N-1,-1,-1,-1,-1)]
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

solve(0,arr)
print(answer)