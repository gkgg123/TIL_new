import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()

def isWin(cha):
    for row in range(0,9,3):
        for dx in range(3):
            x = row+dx
            if lines[x] != cha:
                break
        else:
            return True
    
    for col in range(3):
        for dy in range(0,9,3):
            y = col + dy
            if lines[y] != cha:
                break
        else:
            return True
    if lines[0] == lines[4] == lines[8] == cha:
        return True
    if lines[2] == lines[4] == lines[6] == cha:
        return True
    return False
def solve(arr):
    line = Counter(arr)

    if line[O] + line[X] == 9 and line[X] == line[O]+1:
        if not isWin(O):
            return True
        return False
    elif line[O] == line[X] and isWin(O) and not isWin(X):
        return True
    elif line[O]+1 == line[X] and isWin(X) and not isWin(O):
        return True
    return False
        
O = 'O'
X = 'X'
while True:
    lines = input()
    if lines == 'end':
        break

    if solve(lines):
        print('valid')
    else:
        print('invalid')