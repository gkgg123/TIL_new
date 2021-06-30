def checkWin(play):
    play_num = players[play]

    for x in range(3):
        if arr[x][0] == arr[x][1] == arr[x][2] == play_num:
            return 2
    
    for y in range(3):
        if arr[0][y] == arr[1][y] == arr[2][y] == play_num:
            return 2

    if arr[0][0] == arr[1][1] == arr[2][2] == play_num:
        return 2

    if arr[0][2] == arr[1][1] == arr[2][0] == play_num:
        return 2

    return 0 


def dfs(rc,play):
    global result
    if checkWin((play+1)%2)>1:
        return -1
    if rc <remain_cnt:
        check_result = 10
        for idx in range(remain_cnt):
            if not visited[idx]:
                visited[idx] = True
                x,y = remain_list[idx]
                arr[x][y] = players[play]
                check_result = min(check_result,dfs(rc+1,(play+1)%2))
                visited[idx] = False
                arr[x][y] = 0
        if check_result == 10 or check_result == 0:
            return 0
        else:
            return -check_result
    return 0 
arr = []

# 1 = X
# 2 = O
# 착수하는 사람 부터
cnt_1 = 0
cnt_2 = 0
remain_cnt = 0
remain_list = []
players = [1,2]
for x in range(3):
    temp = list(map(int,input().split()))

    for y in range(3):
        if temp[y] == 1:
            cnt_1 += 1
        elif temp[y] == 2:
            cnt_2 += 1
        else:
            remain_cnt += 1
            remain_list.append((x,y))

    arr.append(temp)
visited = [False for _ in range(remain_cnt)]

start = 0
if cnt_1 > cnt_2:
    start = 1




result = dfs(0,start)
answer = ['D','W','L']
print(answer[result])