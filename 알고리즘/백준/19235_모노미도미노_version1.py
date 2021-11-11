N = int(input())

def check_Row(arr,x,y):
    if arr[x][y] == arr[x][y+1]:
        return True
    return False
def bubble(arr):
    global score
    mini_score = 0
    while True:
        flag = True
        temp = [[0 for _ in range(4)] for _ in range(6)]
        for row in range(5,-1,-1):
            for y in range(4):
                if arr[row][y] == 0:
                    break
            else:
                mini_score += 1
                for y in range(4):
                    arr[row][y] = 0
                flag = False
        if not flag:
            for row in range(5,-1,-1):
                for y in range(4):
                    if arr[row][y] == 0:continue
                    val = arr[row][y]
                    if y<3 and check_Row(arr,row,y):
                        if arr[row][y+1] == arr[row][y]:
                            temp_row = row
                            while temp_row<6 and temp[temp_row][y] == 0 and temp[temp_row][y+1]==0:
                                temp_row += 1
                            temp[temp_row-1][y] = val
                            temp[temp_row-1][y+1] = val
                            arr[row][y+1] = 0 
                    else:
                        temp_row = row
                        while temp_row<6 and temp[temp_row][y] == 0:
                            temp_row += 1
                        temp[temp_row-1][y] = val

                        
        if flag:
            while arr[1].count(0) != 4:
                arr.pop()
                arr.insert(0,[0 for _ in range(4)])
            break
        else:
            arr = [row[:] for row in temp]
    score += mini_score
    return arr





def move(arr,block_type,y,num):
    global score
    if block_type == 1:
        for row in range(6):
            if arr[row][y]:
                arr[row-1][y] = num
                break
        else:
            arr[row][y] = num
    elif block_type == 2:
        for row in range(6):
            if arr[row][y] or arr[row][y+1]:
                arr[row-1][y] = num
                arr[row-1][y+1] = num
                break
        else:
            arr[row][y] = num
            arr[row][y+1] = num
    else:
        for row in range(5):
            if arr[row][y] or arr[row+1][y]:
                arr[row][y] = num
                arr[row-1][y] = num
                break
        else:
            arr[row][y] = num
            arr[row+1][y] = num
    return bubble(arr)

blue_arr = [[0]*4 for _ in range(6)]
green_arr = [[0]*4 for _ in range(6)]


score = 0
for tc in range(1,N+1):
    # 1번 1칸 2번 가로 2칸 3번 세로 2칸
    block_type,x,y = map(int,input().split())
    green_arr = move(green_arr,block_type,y,tc)
    if block_type == 2:
        block_type = 3
    elif block_type == 3:
        block_type = 2
    blue_arr = move(blue_arr,block_type,x,tc)

print(score)
total_block = 0

for row in range(6):
    for col in range(4):
        if blue_arr[row][col]:
            total_block += 1
        if green_arr[row][col]:
            total_block += 1
print(total_block)
