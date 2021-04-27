def find_prime_number():
    global N
    numbers = [True]*(N+1)
    numbers[0] = False
    numbers[1] = False

    for num in range(2,N+1):
        if numbers[num]:
            for num_multi in range(num*2,N+1,num):
                numbers[num_multi] = False
    prime_number = []
    for num in range(N+1):
        if numbers[num]:
            prime_number.append(num)
    return prime_number



N = int(input())


prime_numbers = find_prime_number()
DP = [0]*40001



DP[0] = 1
for prime_number in prime_numbers:
    for num in range(prime_number,N+1):
        DP[num] = (DP[num]+DP[num-prime_number])%123456789


print(DP[N])