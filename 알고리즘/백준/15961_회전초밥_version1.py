from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline
N, D,K,C = map(int,input().split())
a = defaultdict(int)

sushi = deque()
max_value = 0
# D 초밥의 가짓수
# K 는 연속해서 먹은 초밥의 수
# C 쿠폰번호
sushi_dict = defaultdict(int)
cnt = 0
sushi_list = [int(input()) for _ in range(N)]
for left in range(N+K+1):
    sushi_input = sushi_list[left%N]
    if len(sushi)<K:
        sushi.append(sushi_input)
        if sushi_dict[sushi_input] == 0:
            cnt += 1
        sushi_dict[sushi_input] += 1
        if len(sushi) == K:
            if sushi_dict[C]>0:
                max_value = max(max_value,cnt)
            else:
                max_value = max(max_value,cnt+1)
    else:
        remove_sushi = sushi.popleft()
        sushi_dict[remove_sushi] -= 1
        if sushi_dict[remove_sushi] == 0:
            cnt -= 1
        sushi.append(sushi_input)
        if sushi_dict[sushi_input] == 0:
            cnt += 1
        sushi_dict[sushi_input] += 1
        if sushi_dict[C]>0:
            max_value = max(max_value,cnt)
        else:
            max_value = max(max_value,cnt+1)

print(max_value)