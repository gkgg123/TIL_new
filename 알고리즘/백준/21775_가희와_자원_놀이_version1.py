import sys
from collections import deque
input = sys.stdin.readline



N,T = map(int,input().split())

order_list = list(map(int,input().split()))

stack_list = [[[],set()] for _ in range(N+1)]
card_deck = deque()
result = []
for _ in range(T):
    input_list = list(input().split())
    card_deck.append(input_list)

num_occupy_set = set()
for ind in order_list:
    if len(stack_list[ind][0]) > 0:
        cu_card = stack_list[ind][0][0]
        result.append(cu_card[0])
        if cu_card[2] in num_occupy_set:
            continue
        else:
            stack_list[ind][0].pop(0)
            stack_list[ind][1].add(cu_card[2])
            num_occupy_set.add(cu_card[2])

    else:
        cu_card = card_deck.popleft()
        result.append(cu_card[0])

        if cu_card[1] == 'next':
            continue
        elif cu_card[1] == 'acquire':
            if cu_card[2] in num_occupy_set:
                stack_list[ind][0].append(cu_card)
            else:
                stack_list[ind][1].add(cu_card[2])
                num_occupy_set.add(cu_card[2])
        else:
            stack_list[ind][1].remove(cu_card[2])
            num_occupy_set.remove(cu_card[2])

for i in range(T):
    sys.stdout.write(result[i]+"\n")