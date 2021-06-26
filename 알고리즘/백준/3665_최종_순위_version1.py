import sys
from collections import deque
input = sys.stdin.readline
T = int(input())


for tc in range(T):
    N = int(input())
    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    # 전년도 1등부터 ~ N등까지 팀 순서
    prev_order_team = list(map(int,input().split()))
    indegree = [0]*(N+1)
    indegree[0] = float('inf')
    for rank,team_num in enumerate(prev_order_team):
        indegree[team_num] = rank
        for low_team_num in prev_order_team[rank+1:]:
            graph[team_num][low_team_num] = 1

    M = int(input())
    new_indegree = indegree[:]
    for _ in range(M):
        a_team,b_team = map(int,input().split())
        if indegree[a_team] > indegree[b_team]:
            a_team,b_team = b_team,a_team

        # a_team이 상위권 b_team이 하위권 원래는
        graph[b_team][a_team] = 1
        graph[a_team][b_team] = 0
        new_indegree[a_team] += 1
        new_indegree[b_team] -= 1
    indegree = new_indegree[:]
    stack = deque()

    for team_num in range(1,N+1):
        if not indegree[team_num]:
            stack.append(team_num)
    result = []
    if len(stack) == 1:
        cnt = 0
        while cnt<N:
            if not len(stack):
                result = 'IMPOSSIBLE'
                break
            elif len(stack) > 1:
                result = '?'
                break

            cur_node = stack.popleft()
            result.append(cur_node)
            for next_node in range(1,N+1):
                if graph[cur_node][next_node]:
                    indegree[next_node] -= 1
                    if not indegree[next_node]:
                        stack.append(next_node)
            cnt += 1
    elif len(stack) == 0:
        result = 'IMPOSSIBLE'
    else:
        result = '?'
    if type(result) == list:
        print(*result)
    else:
        print(result)