import sys

input = sys.stdin.readline


prime_number = [True]*10000
prime_number[0] = False
prime_number[1] = False

for k in range(2,10000):
    if prime_number[k]:
        for j in range(k+k,10000,k):
            prime_number[j] = False

T = int(input())

for _ in range(T):
    A,B = map(int,input().split())
    if A == B:
        print(0)
    else:
        visited = [True]*10000
        result = 'Impossible'
        stack = [A]
        cnt = 0
        while stack:
            new_stack = set()
            for number in stack:
                for k in [1,10,100,1000]:
                    fall_number = number - (number//k)%10*k
                    for i in range(10):
                        new_number = fall_number + i *k
                        if prime_number[new_number] and visited[new_number] and new_number >= 1000:
                            visited[new_number] = False
                            new_stack.add(new_number)
            if B in new_stack:
                result = cnt + 1
                break
            stack = list(new_stack)[:]
            cnt += 1
        print(result)
