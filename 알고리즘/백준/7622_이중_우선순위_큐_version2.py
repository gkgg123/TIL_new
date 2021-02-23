from collections import deque
import bisect
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    stack = deque()
    stack_dict = dict()
    for _ in range(int(input())):
        command,val = input().split()
        val = int(val)
        if command == 'I':
            if stack_dict.get(val):
                stack_dict[val] += 1
            else:
                bisect.insort_left(stack,val)
                stack_dict[val] = 1
        else:
            if val == 1:
                if stack:
                    last_number = stack[-1]
                    if stack_dict[last_number] == 1:
                        stack_dict.pop(last_number)
                        stack.pop()
                    else: 
                        stack_dict[last_number] -= 1
            else:
                if stack:
                    first_number = stack[0]
                    if stack_dict[first_number] == 1:
                        stack_dict.pop(first_number)
                        stack.popleft()
                    else:
                        stack_dict[first_number] -= 1
    if stack:
        print(stack[-1],stack[0])
    else:
        print('EMPTY')