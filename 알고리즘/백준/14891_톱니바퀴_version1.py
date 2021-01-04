import sys
from collections import deque
# 까다로웠던 점 
# 회전은 전부 판별이 되고 난뒤에, 작동한다
gears =[ list(deque(map(deque,sys.stdin.readline().split()))) for _ in range(4)]

K = int(sys.stdin.readline())
# 12시 0, 3시 2, 9시 6
# N극은 0 S극은 1
for _ in range(K):
    index,rotate = list(map(int,sys.stdin.readline().split()))
    leftindex = index-1
    leftrotate = -rotate
    rightrotate = -rotate
    rightindex = index+1
    rotatelist = []
    while leftindex >=1:
        origingear = list(gears[leftindex][0])
        leftgear = list(gears[leftindex-1][0])
        if origingear[6] == leftgear[2]:
            break
        else:
            rotatelist.append([leftindex-1,leftrotate])
        leftrotate = -leftrotate
        leftindex-=1
    while rightindex <=4:
        origingear = list(gears[rightindex-2][0])
        rightgear = list(gears[rightindex-1][0])
        if origingear[2] == rightgear[6]:
            break
        else:
            rotatelist.append([rightindex-1,rightrotate])
        rightrotate = -rightrotate
        rightindex+=1
    for rotateindex,rotation in rotatelist:
        gears[rotateindex][0].rotate(rotation)
    gears[index-1][0].rotate(rotate)


result = 0

for i in range(4):
    tw = gears[i][0].popleft()
    if tw == '1':
        result += 2**i

print(result)