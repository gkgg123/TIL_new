import sys

def input():
    return sys.stdin.readline().rstrip()

def check(color):
    global arr
    cN = len(color)
    cM = len(color[0])
    for x in range(N-cN+1):
        for y in range(M-cM+1):
            flag = True
            for cx in range(x,x+cN):
                for cy in range(y,y+cM):
                    if arr[cx][cy] and color[cx-x][cy-y]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                for cx in range(x,x+cN):
                    for cy in range(y,y+cM):
                        arr[cx][cy] = arr[cx][cy] + color[cx-x][cy-y]
                return True
    return False

def rotate(color):
    cN = len(color)
    cM = len(color[0])
    new_color = [[0 for _ in range(cN)] for _ in range(cM)]

    for x in range(cN):
        for y in range(cM):
            new_color[y][cN-x-1] = color[x][y]
    return new_color

def solve():

    idx = 0

    while idx<K:
        cur_colorPaper = [row[:] for row in  colorPaper[idx]]
        
        for _ in range(4):
            if check(cur_colorPaper):
                break
            cur_colorPaper = rotate(cur_colorPaper)
            
        idx += 1
    result = 0
    for row in arr:
        result += sum(row)
    return result
N,M,K = map(int,input().split())

colorPaper = []

for _ in range(K):
    cN,cM = map(int,input().split())

    temp = [list(map(int,input().split())) for _ in range(cN)]
    colorPaper.append(temp)

arr = [[0 for _ in range(M)] for _ in range(N)]
print(solve())
