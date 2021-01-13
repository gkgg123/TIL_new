def check(cnt,total,di):
    global result,ccnt
    if cnt == arr[0]:
        temp = 1
        ccnt += 1
        for k in di:
            temp *= arr[dire.index(k)+1]/100
        result += temp
        return
    else:
        cu_x,cu_y = total[-1]
        for i in range(4):
            nx = cu_x + dx[i]
            ny = cu_y + dy[i]
            if (nx,ny) not in total:
                check(cnt+1,total+[(nx,ny)],di+[dire[i]])
    


# 동 서 남 북
dx = [0,0,1,-1]
dy = [1,-1,0,0]
dire = ['E','W','S','N']
arr = list(map(int,input().split()))
result = 0
ccnt = 0
check(0,[(0,0)],[])
print(result)
print(ccnt)