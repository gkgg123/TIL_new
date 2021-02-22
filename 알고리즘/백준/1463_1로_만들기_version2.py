N = int(input())
number_list = [N]
cnt = 0
flag = False
if N == 1:
    print(0)
else:
    while True:
        new_number = []
        for numbers in number_list:
            if numbers == 1:
                flag = True
                break

            if not numbers%3:
                new_number.append(numbers/3)
            if not numbers%2:
                new_number.append(numbers/2)
            new_number.append(numbers-1)
        if flag:
            print(cnt)
            break
        cnt += 1
        number_list = new_number[:]