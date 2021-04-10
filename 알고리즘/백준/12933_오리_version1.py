string = input()
duck = 'quack'
cnt = 0
result = []
answer = 0
for st in string:
    flag = True
    for ind in range(len(result)):
        if duck[(duck.index(result[ind][-1])+1)%5] == st:
            result[ind].append(st)
            flag = False
            break

    if flag:
        if st != 'q':
            answer = -1
            break
        result.append([st])

if answer == -1:
    print(answer)
else:
    for i in result:
        if len(i)%5 != 0:
            print(-1)
            break
    else:
        print(len(result))

    

