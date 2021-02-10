# # 3190 뱀
from collections import deque

N = int(input())
K = int(input())
apples = set(tuple(map(int,input().split())) for _ in range(K))
command_cnt = int(input())
# direction 0동 1남 2서 3북
dx = [0,1,0,-1]
dy = [1,0,-1,0]
commands = []
snakes = deque()
snakes.append((1,1))
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
flag = True
next_time = commands[0][0]
break_flag = False
while True:
    if flag:
        next_time = commands[ind][0]


    snake_times += 1

    snake_head = snakes[0]
    next_x = snake_head[0] + dx[snake_direction]
    next_y = snake_head[1] + dy[snake_direction]
    if 1<= next_x <=N and 1<= next_y<=N:
        if (next_x,next_y) not in snakes:
            if (next_x,next_y) in apples:
                snakes.appendleft((next_x,next_y))
                apples.remove((next_x,next_y))
            else:
                snakes.pop()
                snakes.appendleft((next_x,next_y))
        else:
            break_flag = True
    else:
        break_flag = True
    if break_flag:
        break



    if snake_times == next_time:
        snake_direction = (snake_direction + commands[ind][1])%4
        ind += 1
        print(snake_direction)
        if ind == command_cnt:
            flag = False
    print(snakes)
print(snake_times)