import sys
def custom_sort(arr):
    return sorted(arr,key= lambda x: (x[0],x[1]))

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(float,input().split()))
sort_array = []
for i in range(N):
    sort_array.append((arr[i],1,arr[i]))

sort_array = custom_sort(sort_array)
M = int(input())
answer = sort_array[-1][0] - sort_array[0][0]
while M:
    max_val,cnt,origin = sort_array.pop()
    sort_array.append((origin/(cnt+1),cnt+1,origin))
    sort_array = custom_sort(sort_array)
    answer = min(answer,sort_array[-1][0] - sort_array[0][0])
    M -= 1
print(answer)