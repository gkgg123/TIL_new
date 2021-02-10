# # 3190 뱀
from collections import deque

N = int(input())
K = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    x,y = map(int,input().split())
    board[x][y] = 1

command_cnt = int(input())

# direction 0동 1남 2서 3북
dx = [0,1,0,-1]
dy = [1,0,-1,0]
commands = []
snakes = deque()
snakes.append((1,1))
board[1][1] = 2
for _ in range(command_cnt):
    time,dire = input().split()
    if dire == 'D':
        dire = 1
    else:
        dire = -1
    commands.append((int(time),dire))

snake_times = 0
ind = 0
snake_direction = 0
next_time,next_direction = commands[0]
break_flag = True
while True:


    snake_times += 1

    snake_head = snakes[0]
    next_x = snake_head[0] + dx[snake_direction]
    next_y = snake_head[1] + dy[snake_direction]
    if 1<= next_x <=N and 1<= next_y<=N:
        if board[next_x][next_y] != 2:
            if board[next_x][next_y] == 1:
                snakes.appendleft((next_x,next_y))
                board[next_x][next_y] = 2
            else:
                board[next_x][next_y] = 2
                tail_x,tail_y = snakes.pop()
                board[tail_x][tail_y] = 0
                snakes.appendleft((next_x,next_y))
            break_flag = False
    if break_flag:
        break
    break_flag = True



    if snake_times == next_time:
        snake_direction = (snake_direction + next_direction)%4
        if ind < command_cnt-1:
            ind += 1
            next_time,next_direction = commands[ind]

print(snake_times)