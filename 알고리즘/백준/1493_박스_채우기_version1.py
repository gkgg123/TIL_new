import sys
def input():
    return sys.stdin.readline().rstrip()


L,W,H = map(int,input().split())

N = int(input())
cube_cnt = {}
for _ in range(N):
    x,y = map(int,input().split())
    cube_cnt[x] = y

accumulate_volume = 0
answer = 0
for sq in range(19,-1,-1):
    accumulate_volume *= 8
    if cube_cnt.get(sq):
        cnt = cube_cnt[sq]
        lens = 2**sq
        max_cnt = (L//lens)*(W//lens)*(H//lens) - accumulate_volume
        cur_cnt = min(cnt,max_cnt)
        answer += cur_cnt
        accumulate_volume += cur_cnt


if accumulate_volume == L*W*H:
    print(answer)
else:
    print(-1)