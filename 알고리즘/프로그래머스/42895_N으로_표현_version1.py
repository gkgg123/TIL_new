def solution(N, number):
    dp = [set() for _ in range(9)]
    if N ==number:
        return 1
    dp[1].add(N)
    for idx in range(2,9):
        for i in range(1,idx):
            for number1 in dp[i]:
                for number2 in dp[idx-i]:
                    if number2:
                        for new_number in [number1+number2,number1-number2,number1*number2,number1//number2]:
                            if new_number == number:
                                return idx
                            dp[idx].add(new_number)
                    else:
                        for new_number in [number1+number2,number1-number2,number1*number2]:
                            if new_number == number:
                                return idx
                            dp[idx].add(new_number)
        new_number = int(str(N)*idx)
        if new_number == number:
            return idx
        dp[idx].add(new_number) 
    return -1
print(solution(5,5))