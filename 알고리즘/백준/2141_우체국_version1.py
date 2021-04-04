N = int(input())

arr = []
total_person = 0 
for _ in range(N):
    town,person = map(int,input().split())
    total_person += person
    arr.append([town,person])
arr.sort()
person_list = [k[1] for k in arr]
start = 0
ends = N -1
answer = float('inf')
while start <= ends:
    mid = (start+ends)//2
    left = sum(person_list[:mid+1])
    right = total_person - left
    if left >= right:
        answer = min(arr[mid][0],answer)
        ends = mid - 1
    else:
        start = mid + 1
print(answer)

