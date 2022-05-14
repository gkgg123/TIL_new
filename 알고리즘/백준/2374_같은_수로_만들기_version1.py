import sys

def input():
    return sys.stdin.readline().rstrip()




N = int(input())
stack = []
answer = 0

for _ in range(N):
    number = int(input())
    if stack:
        while stack and stack[-1] < number:
            lower = stack.pop()
            if stack and stack[-1] <= number:
                answer = answer + stack[-1] - lower
            else:
                answer = answer + number-lower
                break
        stack.append(number)

    else:
        stack.append(number)
if stack:
    answer = answer + stack[0] - stack[-1]
print(answer)