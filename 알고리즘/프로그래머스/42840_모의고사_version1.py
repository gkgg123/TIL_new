def solution(answers):
    ans = []
    person3 = [3,3,1,1,2,2,4,4,5,5]
    person2 = [2,1,2,3,2,4,2,5]
    result = [0,0,0]
    for ind,answer in enumerate(answers):
        if answer == (ind)%5+1:
            result[0] += 1
        if answer == person2[ind%len(person2)]:
            result[1] += 1
        if answer == person3[ind%len(person3)]:
            result[2] += 1

    max_result = max(result)
    for k in range(3):
        if result[k] == max_result:
            ans.append(k+1)
    return ans