def solution(n, lost, reserve):
    answer = 0
    student = [0]*(n+1)
    for k in lost:
        student[k] = -1
    for k in reserve:
        student[k] += 1

    for i in range(1,n+1):
        if student[i] > 0:
            for new_student in [i-1,i+1]:
                if 1<=new_student <=n:
                    if student[new_student] == -1:
                        student[i] -= 1
                        student[new_student] += 1
                        break
    for i in range(1,n+1):
        if student[i] >=0:
            answer += 1
    return answer