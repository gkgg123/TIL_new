import sys
def input():
    return sys.stdin.readline().rstrip()

class Point():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

T = int(input())
eps = 10**-9
for _ in range(T):
    N = int(input())
    height_list = [0 for _ in range(N)]
    cross_list = []
    for ind in range(N):
        h,point_len,*point_input = map(int,input().split())
        points = []
        height_list[ind] = h
        for i in range(0,len(point_input),2):
            x,y = point_input[i] , point_input[i+1]
            points.append(Point(x,y))
        
        for i in range(point_len):
            p1,p2 = points[i], points[(i+1)%point_len]
            if (p1.y -eps) * (p2.y - eps) >0:
                continue
            
            x_intercept = -p1.y*((p2.x-p1.x)/(p2.y - p1.y)) + p1.x
            if 0< x_intercept < 100000:
                cross_list.append((x_intercept,ind,i,i+1))

    cross_list.sort()
    stack = []
    for _,ind,_,_ in cross_list:
        if stack and stack[-1] == ind:
            stack.pop()
        else:
            stack.append(ind)
    up_ans = 0
    down_ans = 0
    if len(stack)>=2:
        height = height_list[stack[0]]

        for i in range(1,len(stack)):
            if height_list[stack[i]] > height:
                up_ans += (height_list[stack[i]] - height)
            else:
                down_ans += (-height_list[stack[i]] + height)
            height = height_list[stack[i]]
    print(up_ans,down_ans)
