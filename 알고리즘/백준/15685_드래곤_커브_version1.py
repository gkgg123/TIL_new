import sys


input = sys.stdin.readline
def roll(A,B):
    if A[0] >= B[0] and A[1] < B[1]:
        dx = A[0]-B[0]
        dy = B[1]-A[1]
        return (B[0]+dy,B[1]+dx)
    elif A[0] >= B[0] and A[1] >= B[1]:
        dx = A[0] - B[0]
        dy = A[1] - B[1]
        return (B[0]-dy,B[1]+dx)
    elif A[0] < B[0] and A[1] < B[1]:
        dx = B[0]-A[0]
        dy = B[1]-A[1]
        return (B[0]+dy,B[1]-dx)
    else:
        dx = B[0]-A[0]
        dy = A[1]-B[1]
        return (B[0]-dy,B[1]-dx)



def dragon(cur_gener,total_gener):
    global dragon_list
    if cur_gener == total_gener:
        return

    tail_position = dragon_list[-1]
    dragon_length = len(dragon_list)
    for ind in range(dragon_length-2,-1,-1):
        dragon_list.append(roll(dragon_list[ind],tail_position))
    dragon(cur_gener+1,total_gener)




N = int(input())
# x,y 시작점 d는 시작 방향 g는 세대 

dx = [1,0,-1,0]
dy = [0,-1,0,1]
arr = [[0]*101 for i in range(101)]
for _ in range(N):
    x,y,dire,gener = map(int,input().split())
    dragon_list = [(x,y),(x+dx[dire],y+dy[dire])]
    if gener:
        dragon(0,gener)
    for position in dragon_list:
        arr[position[1]][position[0]] = 1

result = 0



for y in range(100):
    for x in range(100):
        if arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x][y+1] == 4:
            result += 1

print(result)