def solution(new_id):
    answer = ''
    not_string = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id = new_id.lower()
    for item in new_id:
        if item not in not_string:
            answer += item

    while '..' in answer:
        answer = answer.replace('..','.')
    
    
    if answer:

        if answer[0] == '.':
            answer = answer[1:] if answer != '.' else '.'
        if answer[-1] == '.':
            answer = answer[:-1]
    if not answer:
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    while len(answer) <= 2:
        answer += answer[-1]


    return answer



if __name__ == '__main__':
    input_list = ["...!@BaT#*..y.abcdefghijklm",
    "z-+.^.",
    "=.=",
    "123_.def",
    "abcdefghijklmn.p"]
    correct_output = [
        "bat.y.abcdefghi",
        "z--",
        "aaa",
        "123_.def",
        "abcdefghijklmn"
    ]
    ind = 0
    for ts in input_list:
        temp = solution(ts)
        if temp == correct_output[ind]:
            print('옳은답입니다.')
        else:
            print('틀린답입니다.')
        print(temp)
        ind += 1