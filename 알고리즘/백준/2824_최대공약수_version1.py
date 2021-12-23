import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()

def factorization(number_list):
    fact_dict = Counter()

    for num in number_list:

        while num != 1:
            flag = True
            for mod in prime_list:
                if not num%mod:
                    fact_dict[mod] += 1
                    num//=mod
                    flag = False
                    break
            if flag:
                fact_dict[num] += 1
                break


    return fact_dict
def get_prime_number(n):
    prime_number = []
    visited = [True for _ in range(n+1)]
    visited[0] = False
    visited[1] = False

    for num in range(2,int(n**0.5)+1):
        if visited[num]:
            for not_prime in range(num*2,n+1,num):
                visited[not_prime] = False
    
    for num in range(2,n+1):
        if visited[num]:
            prime_number.append(num)
    return prime_number
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

prime_list = get_prime_number(40000)

A_dict = factorization(A)
B_dict = factorization(B)

result = A_dict&B_dict
answer = 1
isBig = False
INF = 10**9
for key in result:
    for _ in range(result[key]):
        answer *= key
        if answer >= INF:
            answer %= INF
            isBig = True
if isBig:
    answer = str(answer).zfill(9)
    print(answer)
else:
    print(answer)