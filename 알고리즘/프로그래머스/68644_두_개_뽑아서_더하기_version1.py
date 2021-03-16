from itertools import combinations
def solution(numbers):
    answer = []
    answer = set(answer)
    for k in combinations(numbers,2):
        answer.add(sum(k))
    answer = list(answer)
    answer.sort()
    return answer