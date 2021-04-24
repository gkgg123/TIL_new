T = int(input())

for _ in range(T):
    day = int(input())

    arr = list(map(int,input().split()))
    answer = 0
    ind = day-1
    max_value = -1
    max_list = []
    while ind >=0:
        if arr[ind] > max_value:
            answer = answer - sum(max_list) + len(max_list)*max_value
            max_list = []
            max_value = arr[ind]
        else:
            max_list.append(arr[ind])

        ind -= 1
    if max_list:
        answer = answer - sum(max_list) + len(max_list)*max_value
    print(answer)