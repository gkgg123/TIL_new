def check():
    for x in range(3):
        prev_num = arr[x][0]
        if not prev_num:continue
        for y in range(1,3):
            if prev_num != arr[x][y]:
                break
        else:
            return prev_num
    
    for y in range(3):
        prev_num = arr[0][y]
        if not prev_num: continue
        for x in range(1,3):
            if prev_num != arr[x][y]:
                break
        else:
            return prev_num

    prev_num = arr[0][0]
    if prev_num:
        for k in range(1,3):
            if prev_num != arr[k][k]:
                break
        else:
            return prev_num
    
    prev_num = arr[0][2]
    if prev_num:
        for k in range(1,3):
            if prev_num != arr[k][2-k]:
                break
        else:
            return prev_num

    return 0


def dfs(rc,player):
    check_num = check()
    if check_num != 0:
        return check_num

    if rc == 0: return -1
    response = []
    for x in range(3):
        for y in range(3):
            if arr[x][y]:continue
            arr[x][y] = player
            response.append(dfs(rc-1,3-player))
            arr[x][y] = 0
    if player in response:return player
    if -1 not in response: return (3-player)
    return -1

arr = [list(map(int,input().split())) for _ in range(3)]
cnt_1 = 0
cnt_2 = 0
player = 1
r_cnt = 0
for x in range(3):
    for y in range(3):
        if arr[x][y] == 1:
            cnt_1 += 1
        elif arr[x][y] == 2:
            cnt_2 += 1
        else:
            r_cnt += 1


if cnt_1 > cnt_2:
    player = 2


result = dfs(r_cnt,player)

if result == -1:
    print('D')
elif result == player:
    print('W')
else:
    print('L')