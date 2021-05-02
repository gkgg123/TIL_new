def check(num):
    visited_numbers = set()
    visited_numbers.add(num)
    if visited[num] == 1:
        return True
    elif visited[num] == 0:
        return False

    while num >= 0:
        temp = 0
        copy_num = num
        while copy_num>0:
            calc_num = copy_num%10
            next_num = copy_num//10
            temp = temp + calc_num**2
            copy_num = next_num
        num = temp
        if temp == 1:
            for vi_num in visited_numbers:
                visited[vi_num] = 1
            return True
        elif temp not in visited_numbers:
            visited_numbers.add(temp)
        else:
            for vi_num in visited_numbers:
                visited[vi_num] = 0
            return False
        


def find_prime_number(N):
    numbers = [True]*(N+1)
    numbers[0] = False
    numbers[1] = False
    prime_list = []
    for num in range(2,N+1):
        if numbers[num]:
            prime_list.append(num)
            for not_prime in range(num+num,N+1,num):
                numbers[not_prime] = False
    return prime_list




N = int(input())


prime_numbers = find_prime_number(N)

visited = [-1]*1000001
result = []

for num in prime_numbers:
    if check(num):
        result.append(num)
for row in result:
    print(row)