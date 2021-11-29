import sys
def input():
    return sys.stdin.readline().rstrip()
T = int(input())
maps = [[0 for _ in range(10001)] for _ in range(10001)]
for tc in range(1,T+1):
    N = int(input())
    result = 0
    mines = []
    for _ in range(N):
        x,y = map(int,input().split())
        maps[x][y] = tc
        mines.append((x,y))

    
    for idx in range(N):
        sx,sy = mines[idx]
        mx = max(0,sx-10)
        my = max(0,sy-10)


        for start_x in range(mx,sx):
            for start_y in range(my,sy):
                end_x = min(start_x+10,10000)
                end_y = min(start_y+10,10000)
                cnt = 0
                for x in range(start_x,end_x+1):
                    for y in range(start_y,end_y+1):
                        if maps[x][y] == tc:
                            cnt += 1
                result = max(cnt,result)
    print(result)