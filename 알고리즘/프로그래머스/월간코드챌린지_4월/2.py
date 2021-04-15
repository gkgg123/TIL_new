from collections import deque
import copy
def solution(s):
    answer = 0
    stack = deque(s)
    for _ in range(len(s)):
        bracket_dict = {'{':0,
        '[':0,
        '(':0}
        check_stack = copy.copy(stack)
        not_flag = False
        for _ in range(len(s)):
            bb = check_stack.popleft()
            if bb in bracket_dict.keys():
                bracket_dict[bb] += 1
            else:
                if bb == ']':
                    if bracket_dict['[']:
                        bracket_dict['['] -= 1
                    else:
                        not_flag = True
                        break
                elif bb == '}':
                    if bracket_dict['{']:
                        bracket_dict['{'] -= 1
                    else:
                        not_flag = True
                        break
                else:
                    if bracket_dict['(']:
                        bracket_dict['('] -= 1
                    else:
                        not_flag = True
                        break
        if not not_flag:
            if sum(bracket_dict.values()) == 0:
                answer +=1


        stack.rotate(-1)

    print(answer)
    
    return answer


solution("[")