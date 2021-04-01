import sys

input = sys.stdin.readline
def calc(operator,x,y):
    if operator == '*':
        return x*y
    elif operator == '-':
        return x-y
    elif operator == '+':
        return x+y
def dfs(idx,value):
    global result
    if idx == length_num-1:
        result = max(result,value)
        return
    temp = calc(operator_list[idx],value,num_list[idx+1])
    dfs(idx+1,temp)

    if idx < length_num-2:
        next_value = calc(operator_list[idx+1],num_list[idx+1],num_list[idx+2])
        temp = calc(operator_list[idx],value,next_value)
        dfs(idx+2,temp)



N = int(input())
origin_input = list(input().strip())
num_list = []
operator_list = []

for ind in range(len(origin_input)):
    if ind%2:
        operator_list.append(origin_input[ind])
    else:
        num_list.append(int(origin_input[ind]))
result = -float('inf')
length_num = len(num_list)

dfs(0,num_list[0])
print(result)