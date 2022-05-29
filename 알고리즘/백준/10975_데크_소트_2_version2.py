import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)
ordered_dict = {}
for idx,num in enumerate(sorted(nums)):
    ordered_dict[num] = idx
deque_list = []

for num in nums:
    if not deque_list:
        deque_list.append(deque([num]))
    else:
        for queue in deque_list:
            if ordered_dict[queue[0]] == ordered_dict[num] + 1:
                queue.appendleft(num)
                break
            elif ordered_dict[queue[-1]] == ordered_dict[num] -1:
                queue.append(num)
                break
        else:
            deque_list.append(deque([num]))

print(len(deque_list))