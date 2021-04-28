L,H,W = map(int,input().split())


arr = [list(input()) for _ in range(H)]
answer = []


for i in range(L):
    start_y = i*W
    flag = False
    for y in range(start_y,start_y+W):
        for x in range(H):
            if arr[x][y] != '?':
                answer.append(arr[x][y])
                flag = True
                break
        if flag:
            break
    else:
        answer.append('?')
print(''.join(answer))
