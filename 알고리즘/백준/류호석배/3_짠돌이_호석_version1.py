
import sys
input = sys.stdin.readline

def combine(a_set,list_b):
    b_set = set()
    
    for x in range(len(list_b)):
        for y in range(len(list_b[0])):
            if list_b[x][y] == '1':
                b_set.add((x,y))
    for dx in range(-50,51):
        for dy in range(-50,51):
            flag = True
            for key in b_set:
                s = (key[0]+dx,key[1]+dy)
                if s in a_set:
                    flag = False
                    break

            if flag:
                row = max()
                result = min(result,(max_X_B-min_X_B+1)*(max_Y_B-min_Y_B+1))

puzzles = {}




for i in range(2):
    N,M = map(int,input().split())
    temp = [list(input().strip()) for _ in range(N)]
    puzzles[i] = temp
    ind = i + 2
    for _ in range(3):
        rotate = []
        for item in zip(*puzzles[ind-2]):
            rotate.append(list(reversed(item)))

        puzzles[ind] = rotate
        ind += 2
result = float('inf')

for ind_a in range(0,2,2):
    a_set = set()
    min_X = float('inf')
    max_X = 0
    min_Y = float('inf')
    max_Y = 0
    for x in range(len(puzzles[ind_a])):
        for y in range(len(puzzles[ind_a][0])):
            if puzzles[ind_a][x][y] == '1':
                a_set.add((x,y))
    
    for ind_b in range(1,9,2):
        combine(a_set,puzzles[ind_b])

print(result)
