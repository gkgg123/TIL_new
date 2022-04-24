import sys
def input():
    return sys.stdin.readline().rstrip()
def solve(turn,point):
    global answer
    if turn == 10:
        answer = max(answer,point)
        return
    move = moves[turn]
    for idx in range(4):
        if horse[idx] == 32:
            continue
        cur_position = horse[idx]
        next_position = horse[idx]
        for i in range(move):
            if next_position == 32:
                break
            if i == 0 and next_position in warp.keys():
                next_position = warp[next_position]
            else:
                next_position = map_maze[next_position]
        if next_position != 32 and next_position in horse:
            continue
        horse[idx] = next_position
        solve(turn+1,point + points[next_position])
        horse[idx] = cur_position
moves = list(map(int,input().split()))

points = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,30,35,22,24,28,27,26,0]
map_maze = [i+1 for i in range(32)]
map_maze[20],map_maze[26],map_maze[28],map_maze[31] = 32,20,24,24
warp = {5 : 21,10:27 , 15:29}

horse = [0,0,0,0]
answer = 0
solve(0,0)
print(answer)