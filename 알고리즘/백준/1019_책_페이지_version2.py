def calc(number,cnt):
    global number_list
    while number > 0:
        number_list[number%10] += cnt
        number = number//10



def solution(start,end):
    global number_list
    cnt = 1
    while start <= end:
        if start%10 != 0:
            while start % 10 != 0 and start <= end:
                calc(start,cnt)
                start += 1
        if start > end:
            break
        if end%10 != 9:
            while end % 10 != 9 and start <= end:
                calc(end,cnt)
                end -= 1
        distance = (end//10 - start//10 + 1)
        for i in range(10):
            number_list[i] += distance * cnt
        cnt *= 10
        start = start//10
        end = end//10







N = int(input())
start = 1
number_list = [0]*10
solution(start,N)
print(*number_list)