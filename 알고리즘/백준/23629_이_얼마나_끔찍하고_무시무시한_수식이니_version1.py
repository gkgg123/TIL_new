from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()
def isNumber(num):
    try:
        int(num)
        return True
    except:
        return False

def convert(num):

    for ind in range(10):
        find_s = str(ind)
        while find_s in num:
            num = num.replace(find_s,alpha[ind])
    return num
def check(arr):
    queue = deque(arr)

    while len(queue)>2:
        num1,operator,num2 = queue.popleft(),queue.popleft(),queue.popleft()
        if isNumber(num1) and isNumber(num2):
            num1 = int(num1)
            num2 = int(num2)
            if operator == '+':
                queue.appendleft(str(num1+num2))
            elif operator == '-':
                queue.appendleft(str(num1-num2))
            elif operator == '/':
                queue.appendleft(str(int(num1/num2)))
            elif operator == 'x':
                queue.appendleft(str(num1*num2))
            else:
                return False,''
        else:
            return False,''
    return True, queue[0]




alpha = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
s = input()

for n in range(10):
    word = alpha[n]
    while word in s:
        s = s.replace(word,str(n))


calc = []
prev = 0
for k in s:
    if k.isnumeric():
        prev = prev*10 + int(k)
    else:
        if prev:
            calc.append(str(prev))
        prev = 0
        calc.append(k)


flag, value = check(calc)
if flag:
    print(''.join(calc))
    print(convert(str(value)))
else:
    print('Madness!')