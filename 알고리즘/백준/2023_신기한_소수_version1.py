
N = int(input())
def makePrimeNumber(num,idx):
    if idx == N:
        result.append(num)
    else:
        for last_num in range(1,10,2):
            new_num = num*10 + last_num
            if isPrime(new_num):
                makePrimeNumber(new_num,idx+1)

def isPrime(num):
    if num in prime_numbers:
        return True
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    prime_numbers.add(num)
    return True


prime_numbers = set([2,3,5,7])
result = []


for num in [2,3,5,7]:
    makePrimeNumber(num,1)
result.sort()

for row in result:
    print(row)