import sys


def prime_num(num):
    sieve = [True]*num
    sieve[1] = False
    m = int(num**0.5) + 1

    for i in range(2, m):
        if sieve[i] == True:
            for j in range(i+i, num, i):
                sieve[j] = False

    return sieve



prime_list = prime_num(10001)
for t in range(int(input())):
    N = int(sys.stdin.readline())
    for number in range(N//2,0,-1):
        other_number = N - number
        if prime_list[other_number] and prime_list[number]:
            print(number,other_number)
            break