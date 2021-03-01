import sys
input = sys.stdin.readline



def check(cnt):
    if cnt == len(check_list):
        for row in sdoku:
            print(*row)
        sys.exit()
    else:
        x,y = check_list[cnt]
        square_ind = x//3*3 + y//3
        for number in range(1,10):
            if row_index[x][number] + col_index[y][number] + square_index[square_ind][number] == 0:
                row_index[x][number] = 1
                col_index[y][number] = 1
                square_index[square_ind][number] = 1
                sdoku[x][y] = number
                check(cnt+1)
                row_index[x][number] = 0
                col_index[y][number] = 0
                square_index[square_ind][number] = 0
                sdoku[x][y] = 0


row_index = [[0]*10 for _ in range(9)]
col_index = [[0]*10 for _ in range(9)]
square_index = [[0]*10 for _ in range(9)]


sdoku = []
check_list = []
for x in range(9):
    input_list = list(map(int,input().split()))

    for y in range(9):
        if input_list[y]:
            row_index[x][input_list[y]] = 1
            col_index[y][input_list[y]] = 1
            square_ind = x//3*3 + y//3
            square_index[square_ind][input_list[y]] = 1
        else:
            check_list.append((x,y))
    sdoku.append(input_list)


check(0)
