import sys

input = sys.stdin.readline
def calc_operator(operator,x,y):
    if operator == '*':
        return x*y
    elif operator == '-':
        return x-y
    elif operator == '+':
        return x+y


def calc():
    new_num_list = []
    new_operator_list = []
    ind = 0
    while ind<len(num_list):
        if ind < len(num_list)-1:
            if not open_bracket[ind]:
                new_num_list.append(num_list[ind])
                new_operator_list.append(operator_list[ind])
                ind += 1
            else:
                new_number = calc_operator(operator_list[ind],num_list[ind],num_list[ind+1])
                if ind == len(num_list)-2:
                    new_num_list.append(new_number)
                else:
                    new_num_list.append(new_number)
                    new_operator_list.append(operator_list[ind+1])
                ind += 2
        else:
            new_num_list.append(num_list[ind])
            ind+= 1
    ind = 0
    value = new_num_list[0]
    while ind < len(new_num_list)-1:
        value = calc_operator(new_operator_list[ind],value,new_num_list[ind+1])
        ind += 1
    return value







def dfs(index):
    global result
    if index == len(num_list)-1:
        result = max(calc(),result)
        return
    else:
        if visited[index]:
            visited[index] = False
            visited[index+1] = False
            open_bracket[index] = True
            dfs(index+1)
            visited[index] = True
            visited[index+1] = True
            open_bracket[index] = False
        dfs(index+1)

N = int(input())
arr = list(input())
if N == 1:
    print(arr[0])
else:
    num_list = []
    operator_list = []
    for i in range(N):
        if i%2:
            operator_list.append(arr[i])
        else:
            num_list.append(int(arr[i]))
    result = -float('inf')
    visited = [True]*len(num_list)
    open_bracket = [False]*len(num_list)
    dfs(0)
    print(result)