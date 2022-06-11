import sys

def input():
    return sys.stdin.readline().rstrip()



exp = list(input())
stack = []
result = []
for d in exp:
    if d.isalpha():
        result.append(d)
    else:
        if d == '(':
            stack.append(d)
        elif d == '*' or d == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                result.append(stack.pop())
            stack.append(d)
        elif d == '+' or d == '-':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(d)
        else:
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
while stack:
    result.append(stack.pop())
print(''.join(result))