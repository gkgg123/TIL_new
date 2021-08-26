import sys
sys.setrecursionlimit(1000000)
def input():
    return sys.stdin.readline().rstrip()

def solution(node,hp,umbrella,dis):
    global result
    x,y = node
    ex,ey = end_node
    end_dis = abs(ex-x) + abs(ey-y)
    if end_dis <= hp + umbrella:
        result = min(result,dis+end_dis)

    for idx in range(umbrella_cnt):
        ux,uy = umbrella_list[idx]
        if not visited_umbrella[idx]:
            next_dis = abs(ux-x) + abs(uy-y)
            if next_dis > umbrella + hp:
                continue
            visited_umbrella[idx] = True
            next_hp = hp - max(0,next_dis-dis-1)
            solution((ux,uy),next_hp,D-1,dis+next_dis)
            visited_umbrella[idx] = False

N,H,D = map(int,input().split())

arr = []
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
    arr.append(temp)
result = float('inf')
umbrella_cnt = len(umbrella_list)
visited_umbrella = [False for _ in range(umbrella_cnt)]
solution(start_node,H,0,0)

if result == float('inf'):
    print(-1)
else:
    print(result)