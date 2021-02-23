


number_list = [True]*1003002
number_list[0] = False
number_list[1] = False
for number in range(2,1003002):
    if number_list[number]:
        for j in range(number+number,1003002,number):
            number_list[j] = False

N = int(input())
flag = False
for find_number in range(N,1003002):
    if number_list[find_number]:
        string_number = str(find_number)
        if len(string_number)%2:
            if len(string_number) != 1:
                a = string_number[:N//2]
                b = string_number[N//2+1::-1]
                if a == b:
                    result = find_number
                    break
            else:
                result = find_number
                break
        else:
            a = string_number[:N//2]
            b = string_number[N//2::-1]
            if a == b:
                result = find_number
                break
    

print(result)