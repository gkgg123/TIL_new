N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

result = float('inf')
for x in range(N):
    for y in range(N):
        for d1 in range(1,y+1):
            for d2 in range(1,N-y+1):
                if 0<=x+d1+d2<N and 0<=y+d2-d1<N and 0<=y+d2<N and 0<=y-d1<N: 
                    max_person = 0
                    min_person = float('inf')
                    visited = [[True]*N for _ in range(N)]
                    temp = 0
                    d1_move = 0
                    d1_flag = True
                    d2_move = 0
                    d2_flag = True
                    for x_five in range(x,x+d2+d1+1):
                        for y_five in range(y-d1_move,y+d2_move+1):
                            visited[x_five][y_five] = False
                            temp += arr[x_five][y_five]
                        if d1_flag:
                            if d1_move == d1:
                                d1_flag = False
                                d1_move -=1
                            else:
                                d1_move += 1
                        else:
                            d1_move -= 1
                        
                        if d2_flag:
                            if d2_move == d2:
                                d2_flag = False
                                d2_move -= 1
                            else:
                                d2_move += 1
                        else:
                            d2_move -= 1
                    max_person = max(max_person,temp)
                    min_person = min(min_person,temp)

                    for x_area,y_area in [[(0,x+d1),(0,y+1)],[(0,x+d2+1),(y+1,N)],[(x+d1,N),(0,y-d1+d2)],[(x+d2+1,N),(y-d1+d2,N)]]:
                        temp = 0
                        for i in range(x_area[0],x_area[1]):
                            for j in range(y_area[0],y_area[1]):
                                if visited[i][j]:
                                    temp += arr[i][j]

                        max_person = max(max_person,temp)
                        min_person = min(min_person,temp)

                    result = min(result,max_person - min_person)

print(result)