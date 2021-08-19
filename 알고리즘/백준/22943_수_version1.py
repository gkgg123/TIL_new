import math
from itertools import permutations
def get_prime_number(max_Num):
    prime_check = [1]*(max_Num+1)
    prime_check[0] = 0
    prime_check[1] = 0
    result = []
    for num in range(2,int(math.sqrt(max_Num))+1):
        if prime_check[num]:
            for new_num in range(num*2,max_Num+1,num):
                prime_check[new_num] = 0
    for num in range(2,max_Num+1):
        if prime_check[num]:
            result.append(num)
    return [prime_check,result]
def check1(num):
    if not num%2:
        if num<=6:
            return False
        for i in range(2,num):
            if prime_check[i] and prime_check[num-i]:
                if i != (num-i):
                    return True
        return False
    elif prime_check[num-2]:
        return True
    return False
def check2(num,M):
    while num%M == 0:
        num //= M
    cnt = 0
    if num<=3:
        return False
    idx = 0
    while num != 1:
        if num%prime_list[idx]:
            idx += 1
        else:
            while not num%prime_list[idx]:
                cnt += 1
                num = num//prime_list[idx]
            idx += 1
        if cnt >2:
            return False
    if cnt == 2:
        return True
    return False


K,M = map(int,input().split())

max_L = 10**(K+1)
prime_check,prime_list = get_prime_number(max_L)
num_str = '0123456789'
answer = 0
for num in permutations(num_str,K):
    if num[0] == '0':
        continue
    else:
        num = int(''.join(num))
        if check1(num):
            if check2(num,M):
                answer += 1
print(answer)

