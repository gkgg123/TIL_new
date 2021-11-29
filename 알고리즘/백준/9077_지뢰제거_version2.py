import sys
def input():
    return sys.stdin.readline().rstrip()
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = 0
    mines = []
    for _ in range(N):
        x,y = map(int,input().split())
        mines.append((x,y))

    mines.sort()
    for idx in range(N):
        for width in range(11):
            cnt = 0
            for next_idx in range(idx,N):
                if mines[idx][0] +10 < mines[next_idx][0]:
                    break
                if mines[idx][1] - width <= mines[next_idx][1] <= mines[idx][1] + 10 -width:
                    cnt += 1
            result = max(cnt,result)
    print(result)