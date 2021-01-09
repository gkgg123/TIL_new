N = int(input())
result = 1

if N == 0:
    print(0)
else:
    for num in range(1,N+1):
        result*=num
    result = str(result)
    cnt = 0
    for k in result[::-1]:
        if k == '0':
            cnt += 1
        else:
            break
    print(cnt)