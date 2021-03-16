def check(t,result):
    if len(result):
        if result[-1] == t:
            result.pop()
            return 2
        else:
            result.append(t)
            return 0
    else:
        result.append(t)
        return 0


def solution(board, moves):
    answer = 0
    lens = len(board)
    result = []
    for k in moves:
        for t in range(lens):
            if board[t][k-1]:
                answer += check(board[t][k-1],result)
                board[t][k-1] = 0
                break
            
    return answer