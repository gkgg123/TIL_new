import sys


def input():
    return sys.stdin.readline().rstrip()
def push_diraction(dire,maze):
    move_arr = [[0 for _ in range(N)] for _ in range(N)]
    sx,sy,ex,ey,gapx,gapy = start_position[dire//2]
    sum_position = set()
    for x in range(sx,ex,gapx):
        for y in range(sy,ey,gapy):
            if maze[x][y]:
                time = 0
                while True:
                    nx = x + dx[dire]*time
                    ny = y + dy[dire]*time
                    if 0<=nx<N and 0<=ny<N:
                        if move_arr[nx][ny]:
                            if move_arr[nx][ny] == maze[x][y] and not maze[nx][ny]%2:
                                move_arr[nx][ny] = move_arr[nx][ny]*2 + 1
                                sum_position.add((nx,ny))
                            else:
                                time -= 1
                                cx = x + dx[dire] * time
                                cy = y + dy[dire] * time
                                move_arr[cx][cy] = maze[x][y]
                            break
                        else:
                            time += 1
                    else:
                        time -= 1
                        cx = x + dx[dire] * time
                        cy = y + dy[dire] * time
                        move_arr[cx][cy] = maze[x][y]
                        break
    if sum_position:
        for x,y in sum_position:
            move_arr[x][y] -= 1
    return move_arr



def solve(idx,maze):
    global  answer
    if idx == 5:
        max_value = max(list(map(max,maze)))
        answer = max(answer,max_value)
        return
    copy_arr = [row[:] for row in maze]

    for x in range(4):
        new_arr = push_diraction(x,copy_arr)
        solve(idx+1,new_arr)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

N = int(input())
start_position = [(0,0,N,N,1,1),(N-1,N-1,-1,-1,-1,-1)]
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

solve(0,arr)
print(answer)