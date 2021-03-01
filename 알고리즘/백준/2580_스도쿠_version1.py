import sys
input = sys.stdin.readline

def check_sdouk(x,y):
    index_set = set(range(1,10))
    occupy_set = set()
    for checky in range(9):
        if sdoku[x][checky]:
            occupy_set.add(sdoku[x][checky])
    for checkx in range(9):
        if sdoku[checkx][y]:
            occupy_set.add(sdoku[checkx][y])
    squarex = x//3*3
    squarey = y//3*3
    for checkx in range(squarex,squarex+3):
        for checky in range(squarey,squarey+3):
            if sdoku[checkx][checky]:
                occupy_set.add(sdoku[checkx][checky])
    return index_set-occupy_set



def sdoku_input(cnt):
    global check_max,result
    if cnt == check_max:
        result = [row[:] for row in sdoku]
        for row in result:
            print(*row)
        sys.exit()
        return
    else:
        a = check_sdouk(*check_list[cnt])
        if a:
            for number in a:
                sdoku[check_list[cnt][0]][check_list[cnt][1]] = number
                sdoku_input(cnt+1)
                sdoku[check_list[cnt][0]][check_list[cnt][1]] = 0
        else:
            return




sdoku = []
check_list = []
for x in range(9):
    input_list = list(map(int,input().split()))

    for y in range(9):
        if not input_list[y]:
            check_list.append((x,y))
    sdoku.append(input_list)
result = []
check_max = len(check_list)
sdoku_input(0)