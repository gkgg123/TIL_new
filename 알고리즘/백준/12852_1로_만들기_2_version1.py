from collections import deque

N = int(input())
if N == 1:
    print(0)
    print(1)
else:
    dp_dict = {N:-1}
    stack = [N]
    cnt = 0
    while stack:
        new_stack = []
        for num in stack:
            if not (num%3 or dp_dict.get(num//3)):
                dp_dict[num//3] = num
                new_stack.append(num//3)
            if not (num%2 or dp_dict.get(num//2)):
                dp_dict[num//2] = num
                new_stack.append(num//2)
            
            if not dp_dict.get(num-1) and num>1:
                dp_dict[num-1] = num
                new_stack.append(num-1)
        cnt += 1
        if 1 in new_stack:
            break
        stack = new_stack[:]
    result = []

    find_num = 1
    print(cnt)
    while True:
        result.append(find_num)
        find_num = dp_dict[find_num]
        if find_num == -1:
            break
    result.reverse()
    print(*result)


