def dfs(cnt):
    if cnt == 81:
        for row in sdoku:
            print(''.join(list(map(str,row))))
        exit()
    else:
        x = cnt//9
        y = cnt%9
        square = (x//3)*3 + y//3
        if sdoku[x][y] == 0:
            for num in range(1,10):
                if not (column_check[y][num] or row_check[x][num] or square_check[square][num]):
                    column_check[y][num] = True
                    row_check[x][num] = True
                    square_check[square][num] = True
                    sdoku[x][y] = num
                    dfs(cnt+1)
                    sdoku[x][y] = 0
                    column_check[y][num] = False
                    row_check[x][num] = False
                    square_check[square][num] = False


        else:
            dfs(cnt+1)



sdoku = []

column_check = [[False for _ in range(10)] for _ in range(9)]
row_check = [[False for _ in range(10)] for _ in range(9)]
square_check =[[False for _ in range(10)] for _ in range(9)]
for x in range(9):
    temp = list(map(int,list(input())))
    for y in range(9):
        if temp[y] != 0:
            square = (x//3)*3 + y//3
            column_check[y][temp[y]] = True
            row_check[x][temp[y]] = True
            square_check[square][temp[y]] = True
    sdoku.append(temp)


dfs(0)