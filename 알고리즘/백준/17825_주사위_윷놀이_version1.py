import sys

def input():
    return  sys.stdin.readline().rstrip()

def solve(turn,point):
    global  answer
    if turn == 10:
        answer = max(answer,point)
        return
    else:

        for idx in range(4):
            move = moves[turn]
            move_position = horse[idx]
            if move_position == 21:
                continue
            prev_position = horse[idx]
            if move_position in warp_point:
                move_position = warp[move_position]
                move -= 1
            if move_position + move <=21:
                move_position = move_position + move
            else:
                for _ in range(move):
                    move_position = next_point[move_position]
            if visited[move_position] and move_position != 21:
                continue
            visited[prev_position],visited[move_position], horse[idx] = 0 , 1, move_position
            solve(turn+1,point+points[move_position])
            visited[prev_position], visited[move_position], horse[idx] = 1,0,prev_position

moves = list(map(int,input().split()))

next_point = [0 for _ in range(33)]
points = [0 for _ in range(33)]
for i in range(21):
    next_point[i] = i+1
    points[i] = i*2
next_point[21] = 21
next_point[22],next_point[23],next_point[24] = 23,24,30
points[22],points[23],points[24] = 13,16,19
next_point[25],next_point[26] = 26,30
points[25],points[26] = 22,24
next_point[27],next_point[28],next_point[29] = 28,29,30
points[27],points[28],points[29] = 28,27,26
next_point[30],next_point[31],next_point[32] = 31,32,20
points[30],points[31],points[32] =25,30,35
warp_point = [5,10,15]
warp = {5 : 22, 10:25 , 15:27}

visited = [0 for _ in range(33)]
horse = [0,0,0,0]
answer = 0
solve(0,0)
print(answer)