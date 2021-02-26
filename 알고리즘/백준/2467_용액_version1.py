N = int(input())


arr = list(map(int,input().split()))

start = 0
end = N-1
index_list = (arr[start],arr[end])
result = arr[end]+arr[start]

while start<end:
    temp = arr[end]+arr[start]
    if abs(result) > abs(temp):
        result = temp
        index_list = (arr[start],arr[end])
        if result == 0:
            break
    if temp >= 0:
        end -= 1
    else:
        start += 1


print(*index_list)