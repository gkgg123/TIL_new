import sys

def input():
    return sys.stdin.readline().rstrip()

def check_pick(pick_list,point):
    x,y = point
    for nx,ny in pick_list:
        if abs(nx-x) == abs(ny-y):
            return False
    return True

def dfs(problem_list,start,pick_list,color):
    global result
    if len(problem_list) == start:
        result[color] = max(result[color],len(pick_list))
        return
    else:

        for idx in range(start,len(problem_list)):
            x,y = problem_list[idx]
            if check_pick(pick_list,(x,y)):
                dfs(problem_list,idx+1,pick_list+[(x,y)],color)


N = int(input())


arr = [list(map(int,input().split())) for _ in range(N)]

result = 0
black_set = []
white_set = []
for x in range(N):
    for y in range(N):
        if arr[x][y]:
            if (x+y)%2:
                white_set.append((x,y))
            else:
                black_set.append((x,y))

result = [0,0]
dfs(black_set,0,[],0)
dfs(white_set,0,[],1)

print(sum(result))