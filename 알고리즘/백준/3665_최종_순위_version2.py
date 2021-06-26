import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    prev_rank = [0]*(N+1)
    current_rank = [0]*(N+1)
    arr = list(map(int,input().split()))
    for i in range(N):
        prev_rank[arr[i]] = i +1
        current_rank[arr[i]] = i + 1

    M = int(input())

    for _ in range(M):
        a_team,b_team = map(int,input().split())

        if prev_rank[a_team] > prev_rank[b_team]:
            current_rank[a_team] -= 1
            current_rank[b_team] += 1
        else:
            current_rank[a_team] += 1
            current_rank[b_team] -= 1

    result = [0]*(N+1)
    flag= False
    for team_num in range(1,N+1):
        if result[current_rank[team_num]]:
            flag = True
            break
        else:
            result[current_rank[team_num]] = team_num

    if flag:
        print('IMPOSSIBLE')
    else:
        print(*result[1:])
