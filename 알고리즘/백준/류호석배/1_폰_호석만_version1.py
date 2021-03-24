import sys
Base_string = {}
for number in range(ord('0'),ord('9')+1):
    Base_string[chr(number)] = number - 48
for alpha in range(ord('a'),ord('z')+1):
    Base_string[chr(alpha)] = alpha - 87
A,B = input().split()
a = {}
b = {}

for i in range(2,37):
    temp_a = 0
    a_ind = 0
    for k in range(len(A)-1,-1,-1):
        num = Base_string[A[k]]
        if num >= i:
            break
        T = i**(len(A)-1 - k)
        temp_a = temp_a + num * T
    else:
        if temp_a < 2**63:
            if a.get(temp_a):
                a[temp_a].append(i)
            else:
                a[temp_a] = [i]
    temp_b = 0
    for k in range(len(B)-1,-1,-1):
        num = Base_string[B[k]]
        if num >= i:
            break
        T = i**(len(B)-1 - k)
        temp_b = temp_b + num * T
    else:
        if temp_b < 2**63:
            if b.get(temp_b):
                b[temp_b].append(i)
            else:
                b[temp_b] = [i]
answer = list(set(a.keys())&set(b.keys()))
if len(answer) == 1:
    if len(a[answer[0]]) == 1 and len(b[answer[0]]) == 1:
        if a[answer[0]][0] != b[answer[0]][0]:
            print(answer[0],a[answer[0]][0],b[answer[0]][0])
        else:
            print('Impossible')
    
    else:
        print('Multiple')
elif len(answer) > 1:
    print('Multiple')
else:
    print('Impossible')
