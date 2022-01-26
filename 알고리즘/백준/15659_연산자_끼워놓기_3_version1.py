import sys


def input():
    return sys.stdin.readline().rstrip()

def dfs(idx,stack):
    global min_val,max_val
    if idx == N:
        new_stack = []
        while stack:
            cur = stack.pop(0)
            if cur in operator:
                if operator[cur]>1:
                    prev_num = new_stack.pop()
                    next_num = stack.pop(0)
                    if operator[cur] == 2:
                        new_stack.append(prev_num*next_num)
                    else:
                        new_stack.append(prev_num//next_num)
                else:
                    new_stack.append(cur)
            else:
                new_stack.append(cur)
        stack = new_stack[:]
        new_stack = []
        while stack:
            cur = stack.pop(0)
            if cur in operator:
                prev_num = new_stack.pop()
                next_num = stack.pop(0)
                if operator[cur]:
                    new_stack.append(prev_num - next_num)
                else:
                    new_stack.append(prev_num + next_num)
            else:
                new_stack.append(cur)
        min_val = min(min_val,new_stack[0])
        max_val = max(max_val,new_stack[0])            
    else:
        for i in range(4):
            if count[i]:
                count[i] -= 1
                dfs(idx+1,stack +[op[i],arr[idx]])
                count[i] += 1

N = int(input())

arr = list(map(int,input().split()))

# + , - , *, /
operator = {'+':0,'-':1,'*':2,'/':3}
op = ['+','-',"*",'/']
count = list(map(int,input().split()))

min_val = float('inf')
max_val = -float('inf')

dfs(1,[arr[0]])

print(max_val)
print(min_val)