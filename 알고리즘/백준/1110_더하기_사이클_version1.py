s = int(input())
e = s
cnt = 0
while True:
    s = (s//10+s%10)%10 + (s%10)*10
    cnt += 1
    if e == s:
        break
print(cnt)