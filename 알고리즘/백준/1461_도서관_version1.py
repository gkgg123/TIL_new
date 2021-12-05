import sys

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
def solve(numbers):
    len_K = len(numbers)//M
    temp = 0
    while len_K:
        temp += numbers.pop()
        for _ in range(M-1):
            numbers.pop()
        len_K -= 1
    if numbers:
        temp += numbers[-1]
    return temp*2

arr = list(map(int,input().split()))
p_l = []
m_l = []
max_value = 0
for num in arr:
    if num>=0:
        p_l.append(num)
        if max_value < num:
            max_value = num
    else:
        m_l.append(-num)
        if max_value < -num:
            max_value = -num
p_l.sort()
m_l.sort()
print(solve(p_l)+solve(m_l)-max_value)
