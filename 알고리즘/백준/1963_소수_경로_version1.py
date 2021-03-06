import sys

input = sys.stdin.readline
def findprimenumber():
    global prime_number
    prime_number[1] = False
    prime_number[0] = False
    for i in range(2,10001):
        if prime_number[i]:
            for j in range(i+i,10001,i):
                prime_number[j] = False





T = int(input())
prime_number = [True]*10001
findprimenumber()
for _ in range(T):
    A,B = map(int,input().split())
    result = 'Impossible'
    visited = [-1] * 10001
    if A == B:
        print(0)
    else:
        stack = [A]
        cnt = 0
        while stack:
            new_stack = []
            for number in stack:
                number_list = list(map(int,list(str(number))))
                for ind in range(4):
                    if ind == 0:
                        for k in range(1,10):
                            if number_list[ind] != k:
                                new_number = k*1000 + 100*number_list[1] + 10*number_list[2] + number_list[3]
                                if visited[new_number] == -1 and prime_number[new_number]:
                                    visited[new_number] = cnt+1
                                    new_stack.append(new_number)
                    else:
                        for k in range(10):
                            if number_list[ind] != k:
                                new_number = number - number_list[ind]*(10**(3-ind)) + k*(10**(3-ind))
                                if visited[new_number] == -1 and prime_number[new_number]:
                                    visited[new_number] = cnt+1
                                    new_stack.append(new_number)
            if B in new_stack:
                result = cnt + 1
                break
            stack = new_stack[:]
            cnt += 1
        print(result)
        
        
