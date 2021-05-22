import math
import sys

input = sys.stdin.readline

def get_prim_number(N):
    prime_check = [True]*(N+1)
    prime_check[0] = False
    prime_check[1] = False
    result = []

    for num in range(2,int(math.sqrt(N))+1):
        if prime_check[num]:
            for new_num in range(num*2,N+1,num):
                prime_check[new_num] = False
    for num in range(2,N+1):
        if prime_check[num]:
            result.append(num)
    return result


N = int(input().strip())

prime_list = get_prim_number(N)
interval_sum = 0
left = 0
cnt = 0
for right in range(len(prime_list)):
    interval_sum += prime_list[right]

    while interval_sum > N:
        interval_sum -= prime_list[left]
        left += 1

    if interval_sum == N:
        cnt += 1

print(cnt)
