# 	babygranfa 코드 분석
arr = list(input())
N = len(arr)
left_bracket = 0
right_bracket = 0
total_sum = 0
left_stack = []
right_stack = []
left_list = [0]*N
right_list = [0]*N

for i in range(N):
    if arr[i] == '(':
        left_bracket += 1
        total_sum += 1
        left_stack.append(i)
    else:
        right_bracket += 1
        total_sum -= 1
        if left_stack:
            left_stack.pop()
        else:
            right_stack.append(i)
    
    left_list[i] = left_bracket
    right_list[i] = right_bracket

if total_sum > 0:
    print(left_list[-1] - left_list[left_stack[-1]]+1)
elif total_sum <0:
    print(right_list[right_stack[0]])
else:
    print(0)