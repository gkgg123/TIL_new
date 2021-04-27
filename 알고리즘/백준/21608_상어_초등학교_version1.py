
def find_favorite_seat(num,fa_list):
    max_list = [[[] for _ in range(5)] for _ in range(5)]
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                favorite_cnt = 0
                empty_cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<N:
                        if arr[nx][ny] == 0:
                            empty_cnt += 1
                        elif arr[nx][ny] in favorite_students:
                            favorite_cnt += 1
                max_list[favorite_cnt][empty_cnt].append((x,y))

    for fa_c in range(4,-1,-1):
        for em_c in range(4,-1,-1):
            if max_list[fa_c][em_c]:
                max_list[fa_c][em_c].sort()
                arr[max_list[fa_c][em_c][0][0]][max_list[fa_c][em_c][0][1]] = num
                return
                    
            




N = int(input())
# (r행 c열)

arr = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
student_dict = {}
for _ in range(N**2):
    input_list = list(map(int,input().split()))
    student_number = input_list[0]
    favorite_students = set(input_list[1:])
    student_dict[student_number] = favorite_students
    find_favorite_seat(student_number,favorite_students)

fill_gage = [0,1,10,100,1000]

result = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        num = arr[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx<N and 0<=ny<N:
                if arr[nx][ny] in student_dict[num]:
                    cnt += 1

        result += fill_gage[cnt]

print(result)

