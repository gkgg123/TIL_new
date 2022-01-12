import sys


def input():
    return sys.stdin.readline().rstrip()


def check(cardpack_cnt):
    pack_cnt = 0
    start = 0

    while cardpack_cnt + start <=N:
        dup = dict()
        for idx in range(start,start+cardpack_cnt):
            if cards[idx] not in dup:
                dup[cards[idx]] = idx
            else:
                start = dup[cards[idx]] + 1
                break
        else:
            pack_cnt += 1
            start = start + cardpack_cnt
    return pack_cnt

N,M = map(int,input().split())


cards = list(map(int,input().split()))


left = 1

right = N//M+1
while left+1<right:
    mid = (left+right)//2
    if check(mid)>=M:
        left = mid
    else:
        right = mid


print(left)