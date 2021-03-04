from itertools import permutations
from collections import deque
def outOfrange(x,y):
    if 0 > x or x >3 or y<0 or y>3:
        return True
    return False

def dfs(start,end,copy_board):
    dp = [[-1]*4 for _ in range(4)]
    dp[start[0]][start[1]] = 0
    stack = deque()
    stack.append((start[0],start[1]))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while stack:
        x,y = stack.popleft()
        for i in range(4):
            repeat = 0
            while True:
                nx = x + dx[i]*repeat
                ny = y + dy[i]*repeat
                if outOfrange(nx+dx[i],ny+dy[i]) or (repeat!=0 and copy_board[nx][ny]):
                    break
                repeat += 1
            for re in (1,repeat):
                nx = x + dx[i] * re
                ny = y + dy[i] * re
                if outOfrange(nx,ny):
                    continue
                if dp[nx][ny] == -1:
                    dp[nx][ny] = dp[x][y] + 1
                    stack.append((nx,ny))
                    if dp[end[0]][end[1]] != -1:
                        return dp[end[0]][end[1]]
    return dp[end[0]][end[1]]



def find_command(x,y,find_card,copy_board):
    dis1 = dfs((x,y),find_card[0],copy_board)
    dis2 = dfs(find_card[0],find_card[1],copy_board)
    return dis1+dis2
        



def solution(board, r, c):
    answer = float('inf')
    card_list = [[] for _ in range(7)]
    card_numbers = set()
    for x in range(4):
        for y in range(4):
            if board[x][y]:
                card_list[board[x][y]].append((x,y))
                card_numbers.add(board[x][y])

    card_cnt = len(card_numbers)
    for combi in permutations(card_numbers):
        predict_dict = {}
        for k in range(1<<card_cnt):
            distance = 0
            mouse_cursor_x = r
            mouse_cursor_y = c
            copy_board = [row[:] for row in board]
            temp = ''
            for ind,num in enumerate(combi):
                start = int(bool((k&1<<(ind))))
                end = (start+1)%2
                temp += str(start)
                find_card = [card_list[num][start],card_list[num][end]]
                if not predict_dict.get(temp):
                    distance += find_command(mouse_cursor_x,mouse_cursor_y,find_card,copy_board)
                    predict_dict[temp] = distance
                else:
                    distance = predict_dict[temp]
                mouse_cursor_x = card_list[num][end][0]
                mouse_cursor_y = card_list[num][end][1]
                copy_board[card_list[num][start][0]][card_list[num][start][1]] = 0
                copy_board[card_list[num][end][0]][card_list[num][end][1]] = 0
                if distance > answer:
                    break
            if answer > distance:
                answer = distance
    return answer+2*card_cnt


a = solution([[1,0,2,0],[6,2,4,0],[0,0,1,0],[6,0,0,4]],1,0)
print(a)