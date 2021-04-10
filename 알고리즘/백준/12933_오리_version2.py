S = input()

duck = {'q':0,'u':1,'a':2,'c':3,'k':4}

queue = []
answer = 0
for sound in S:
    flag = True
    for ind in range(len(queue)):
        if (queue[ind] + 1)%5 == duck[sound]:
            queue[ind] = (queue[ind] + 1)%5
            flag = False
            break
    if flag:
        if duck[sound] != 0:
            answer = -1
            break
        queue.append(0)


if answer == -1:
    print(-1)
else:
    for num in queue:
        if num != 4:
            print(-1)
            break
    else:
        print(len(queue))
