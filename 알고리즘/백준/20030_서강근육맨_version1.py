N = int(input())

arr = list(map(int,input().split()))

arr.sort()
min_value = 0
if len(arr)%2:
    min_value = arr.pop()
    lens = len(arr)//2
    for _ in range(lens):
        t = arr.pop() + arr.pop(0)
        min_value = max(min_value,t)
else:
    lens = len(arr)//2
    for _ in range(lens):
        t = arr.pop() + arr.pop(0)
        min_value = max(min_value,t)
print(min_value)