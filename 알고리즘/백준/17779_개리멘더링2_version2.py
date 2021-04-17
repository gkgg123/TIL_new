def get_points(N):
    temp = []
    for x in range(1,N-1):
        for y in range(2,N):
            for d1 in range(1,y):
                for d2 in range(1,N-y+1):
                    if x + d1 + d2 >N:
                        break
                    temp.append([x,y,d1,d2])
    return temp

def divide_city(x,y,d1,d2):
    board = [[0]*N for _ in range(N)]
    for i in range(x+d1):
        for j in range(y):
            board[i][j] = 1
    
    for i in range(x+d2):
        for j in range(y,N):
            board[i][j] = 2

    for i in range(x+d1-1,N):
        for j in range(y-d1+d2-1):
            board[i][j] = 3

    for i in range(x+d2,N):
        for j in range(y-d1+d2-1,N):
            board[i][j] = 4

    for i in range(d1+d2+1):
        for j in range(-(d1-abs(i-d1)), d2+1-abs(i-d2)):
            board[x+i-1][y+j-1] = 5

    return board


N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

divide_possible_list = get_points(N)

result = float('inf')
for x,y,d1,d2 in divide_possible_list:
    board = divide_city(x,y,d1,d2)
    persons = [0]*5
    for i in range(N):
        for j in range(N):
            persons[board[i][j]-1] += arr[i][j]

    diff = max(persons) - min(persons)
    if diff < result:
        result = diff
print(result)
