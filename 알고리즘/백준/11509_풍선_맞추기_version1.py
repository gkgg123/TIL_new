import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = list(map(int,input().split()))

answer = 0

shoot_cnt = [0 for _ in range(max(arr)+1)]

for num in arr:
    if shoot_cnt[num]:
        shoot_cnt[num] -= 1
        shoot_cnt[num-1] += 1
    else:
        answer += 1
        shoot_cnt[num-1] += 1

print(answer)