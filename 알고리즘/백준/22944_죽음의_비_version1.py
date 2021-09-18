import sys
def input():
    return sys.stdin.readline().rstrip()
def solution(x,y,hp,umbrella,dis):
    global result
    ex,ey = end_node
    end_dis = abs(ex-x) + abs(ey-y)
    if end_dis <= hp + umbrella:
        result = min(result,dis+end_dis)
        return

    for idx in range(umbrella_cnt):
        ux,uy = umbrella_list[idx]
        next_dis = abs(ux-x) + abs(uy-y)
        if visited_umbrella[idx] or next_dis > umbrella+hp:
            continue
        visited_umbrella[idx] = True
        next_hp = hp
        if umbrella < next_dis:
            next_hp = hp - next_dis + umbrella
        solution(ux,uy,next_hp,D,dis+next_dis)
        visited_umbrella[idx] = False

N,H,D = map(int,input().split())

start_node = []
end_node = []
umbrella_list = []
for x in range(N):
    temp = list(input())

    for y in range(N):
        if temp[y] == 'S':
            start_node = (x,y)
        elif temp[y] == 'E':
            end_node = (x,y)
        elif temp[y] == 'U':
            umbrella_list.append((x,y))
result = float('inf')
umbrella_cnt = len(umbrella_list)
visited_umbrella = [False for _ in range(umbrella_cnt)]
solution(start_node[0],start_node[1],H,0,0)
if result == float('inf'):
    print(-1)
else:
    print(result)