arr = list(input())
N = len(arr)
left_bracket = 0
right_bracket = 0
total_bracket = 0
result = 0
for i in range(N):
    if arr[i] == '(':
        left_bracket += 1
        total_bracket += 1
    else:
        right_bracket += 1
        total_bracket -= 1

    if total_bracket <= 1:
        left_bracket = 0

    if total_bracket == -1:
        result = right_bracket
        break


if total_bracket > 0:
    result = left_bracket

print(result)

