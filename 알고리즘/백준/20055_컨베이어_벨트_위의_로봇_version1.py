from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ls = [['X'] for _ in range(2*n)]
for i in range(2*n):
    ls[i].append(arr[i])
belt = deque(ls)
lift_idx = 0
drop_idx = n-1
cnt = 0 
result = 0
while True:
    #내구도가 0인게 k개 이상인지 카운트해서 while문 탈출조건을 세워준다.
    if cnt >= k:
        break
    # 벨트 돌아가기
    tmp = belt.pop()
    belt.appendleft(tmp)
    # 내릴 수 있으면 내린다.
    if belt[drop_idx][0] == 'O':
        belt[drop_idx][0] = 'X'
    #이동이 가능하면 이동한다.
    for i in range(n-2,-1,-1):
        if belt[i][0] == 'O':
            if belt[i+1][0] == 'X' and belt[i+1][1] != 0:
                belt[i][0] = 'X'
                belt[i+1][0] = 'O'
                belt[i+1][1] -= 1
                if i+1 == drop_idx:
                   belt[i+1][0] = 'X'
    #로봇을 올린다.
    if belt[lift_idx][1] != 0 and belt[lift_idx][0] == 'X':
        belt[lift_idx][0] = 'O'
        belt[lift_idx][1] -= 1
    cnt = 0
    for i in range(len(belt)):
        if belt[i][1] == 0: 
            cnt += 1
    result += 1
                
print(result)