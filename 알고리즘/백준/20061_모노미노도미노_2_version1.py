N = int(input())

def bubble(arr,tc):
    global score
    all_row = set(range(6))
    remove_arr = set()
    empty_arr = set()
    for row in range(5,-1,-1):
        if sum(arr[row]) == 4:
            remove_arr.add(row)
        elif not sum(arr[row]):
            empty_arr.add(row)

    remain_row = sorted(list(all_row - remove_arr - empty_arr))
    temp = []
    while len(remain_row) > 4:
        remain_row.pop()

    for _ in range(6-len(remain_row)):
        temp.append([0]*4)
    for row in remain_row:
        temp.append(arr[row][:])
    score += len(remove_arr)
    return temp





def move(arr,block_type,x,y,tc):
    global score
    if block_type == 1:
        for row in range(6):
            if arr[row][y]:
                arr[row-1][y] = 1
                break
        else:
            arr[row][y] = 1
    elif block_type == 2:
        for row in range(6):
            if arr[row][y] or arr[row][y+1]:
                arr[row-1][y] = 1
                arr[row-1][y+1] = 1
                break
        else:
            arr[row][y] = 1
            arr[row][y+1] = 1
    else:
        for row in range(5):
            if arr[row][y] or arr[row+1][y]:
                arr[row][y] = 1
                arr[row-1][y] = 1
                break
        else:
            arr[row][y] = 1
            arr[row+1][y] = 1
    return bubble(arr,tc)

blue_arr = [[0]*4 for _ in range(6)]
green_arr = [[0]*4 for _ in range(6)]


score = 0
for tc in range(N):
    # 1번 1칸 2번 가로 2칸 3번 세로 2칸
    block_type,x,y = map(int,input().split())
    green_arr = move(green_arr,block_type,x,y,tc)
    if block_type == 2:
        block_type = 3
    elif block_type == 3:
        block_type = 2
    blue_arr = move(blue_arr,block_type,y,x,tc)

print(score)
total_block = sum(map(sum,green_arr)) + sum(map(sum,blue_arr))
print(total_block)