import sys
def input():
    return  sys.stdin.readline().rstrip()
def solve(F,cnt):

    for _ in range(cnt):
        temp = [None for _ in range(12)]
        for x in range(12):
            temp[x] = cube[rotate[F][x]]
        for x in range(12):
            cube[rotate[F][x]] = temp[(x+3)%12]
        temp = [[None for _ in range(3)] for _ in range(3)]
        for ind in range(9):
            x,y = ind//3, ind%3
            temp[y][2-x] = cube[F*9 + ind]
        for ind in range(9):
            x,y = ind//3, ind%3
            cube[F*9 + ind] = temp[x][y]
T = int(input())
face = ['w','o','g','r','b','y']
number = {
    'U' : 0,
    'D' : 5,
    'F' : 3,
    'B' : 1,
    'L' : 2,
    'R' : 4,
    '+' : 1,
    '-' : 3
}
rotate = [
    [9,10,11,18,19,20,27,28,29,36,37,38],
    [24,21,18,0,1,2,38,41,44,53,52,51],
    [6,3,0,11,14,17,51,48,45,33,30,27],
    [8,7,6,20,23,26,45,46,47,42,39,36],
    [29,32,35,47,50,53,15,12,9,2,5,8],
    [35,34,33,26,25,24,17,16,15,44,43,42]
]
init_cube = []
for val in face:
    init_cube.extend([val for _ in range(9)])
for _ in range(T):
    N = int(input())
    commands = list(input().split())
    cube = init_cube[:]
    for command in commands:
        solve(number[command[0]],number[command[1]])
    for x in range(3):
        print(''.join(cube[3*x:3*x+3]))
