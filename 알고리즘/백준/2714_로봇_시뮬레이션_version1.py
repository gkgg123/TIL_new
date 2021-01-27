# 2714 로봇 시뮬레이션
# A,B, A은 가로, B는 세로 N은 로봇들
# L,R,F : 로봇기준 왼쪽 90도, 로봇방향 기준 오른쪽 90도, 로봇 기준 앞으로 GO
# 잘못된 명령 : Robot X crashes into the wall: X번 로봇이 벽에 충돌
# Robot X crashes into robot Y : X번 로봇이 Y번 로봇에 부딪힘
def rotate_dire(rotate,current):
    dire_left = [3,0,1,2]
    dire_right = [1,2,3,0]
    if rotate == 'L':
        return dire_left[current]
    else:
        return dire_right[current]


def display_crash(flag,*numbers):
    if flag:
        return f'Robot {numbers[0]} crashes into the wall'
    else:
        return f'Robot {numbers[0]} crashes into robot {numbers[1]}'


A,B = map(int,input().split())
N,M = map(int,input().split())
robots = {}
robot_place = {}
#  E : 0 , S : 1 , W : 2 , N : 3
dire_match = {'E':0,'S':1,'W':2,'N':3}
for robot_number in range(1,N+1):
    X,Y,dire = input().split()
    robots[robot_number]= (int(X),int(Y),dire_match[dire])
    robot_place[(int(X),int(Y))] = robot_number
command_list = []
for _ in range(M):
    robot_number,command,repeat = input().split()
    command_list.append((int(robot_number),command,int(repeat)))

flag = True
result = 'OK'
go_robots = [(1,0),(0,-1),(-1,0),(0,1)]


for command_robot,command,repeat in command_list:
    cu_X, cu_Y,cu_dire = robots[command_robot]
    del robot_place[(cu_X,cu_Y)]
    for _ in range(repeat):
        if command == 'F':
            next_X = cu_X + go_robots[cu_dire][0]
            next_Y = cu_Y + go_robots[cu_dire][1]
            if 1<= next_X <= A  and 1<= next_Y <= B:
                if robot_place.get((next_X,next_Y)):
                    flag = False
                    result = display_crash(False,command_robot,robot_place[(next_X,next_Y)])
                    break
                else:
                    cu_X = next_X
                    cu_Y = next_Y

            else:
                flag = False
                result = display_crash(True,command_robot)
                break 
        else:
            cu_dire = rotate_dire(command,cu_dire)

    robots[command_robot] = (cu_X,cu_Y,cu_dire)
    robot_place[(cu_X,cu_Y)] = command_robot
    if not flag:
        break


print(result)