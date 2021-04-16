N = int(input())
arr = list(map(int,input().split()))

B,C = map(int,input().split())
answer = 0
for num in arr:
    num -= B
    answer += 1
    if num > 0:
        answer = answer + num//C + (0 if num%C == 0 else 1)
print(answer)