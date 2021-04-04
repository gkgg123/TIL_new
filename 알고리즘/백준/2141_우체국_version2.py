import sys
input = sys.stdin.readline

N = int(input())
total_person = 0
arr = []
for _ in range(N):
    town,person = map(int,input().split())
    total_person += person
    arr.append([town,person])

arr.sort()
left_person = 0
ind = 0
while left_person < total_person/2:
    left_person += arr[ind][1]
    ind += 1
print(arr[ind-1][0])
