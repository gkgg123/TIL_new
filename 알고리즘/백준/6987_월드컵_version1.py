def founded(cnt):
    global result
    if cnt == 15:
        if sum(list(map(sum,win_draw_defeat))) == 0:
            result = 1
            return
    else:
        origin_number = origin_team[cnt]
        next_number = next_team[cnt]
        for idx in range(3):
            origin_team_score = idx
            next_team_score = 2-idx
            if win_draw_defeat[origin_number][origin_team_score] > 0 and win_draw_defeat[next_number][next_team_score]:
                win_draw_defeat[origin_number][origin_team_score] -= 1
                win_draw_defeat[next_number][next_team_score] -= 1
                founded(cnt+1)
                win_draw_defeat[origin_number][origin_team_score] += 1
                win_draw_defeat[next_number][next_team_score] += 1


from collections import deque
origin_team = [0,0,0,0,0,1,1,1,1,2,2,2,3,3,4]
next_team = [1,2,3,4,5,2,3,4,5,3,4,5,4,5,5]
answer = []
for _ in range(4):
    score = deque(map(int,input().split()))
    win_draw_defeat = []
    result = 0
    for _ in range(6):
        temp = []
        for _ in range(3):
            temp.append(score.popleft())
        win_draw_defeat.append(temp)
    founded(0)
    answer.append(result)
print(*answer)