import bisect

def solution(info, query):
    answer = []
    index_dict = {'-':0,
    'cpp': 1,
    'java':2,
    'python': 3,
    'backend':1,
    'frontend' :2,
    'junior':1,
    'senior':2,
    'chicken':1,
    'pizza':2,
    }
    store_query = [[] for _ in range(108)]
    for info_string in info:
        language,position,career,soulfood,score = info_string.split(' ')
        score = int(score)
        for ind1 in [0,index_dict[language]]:
            for ind2 in [0,index_dict[position]]:
                for ind3 in [0,index_dict[career]]:
                    for ind4 in [0,index_dict[soulfood]]:
                        ind = ind1*27 + ind2*9 + ind3*3 + ind4
                        store_query[ind].append(score)
    for ind in range(108):
        store_query[ind].sort()
    for qu in query:
        language,position,career,last_query = map(str.strip,qu.split('and'))
        soulfood,score = last_query.split(' ')
        score = int(score)
        ind = index_dict[language]*27 + index_dict[position]*9 + index_dict[career]*3 + index_dict[soulfood]
        cnt = len(store_query[ind]) - bisect.bisect_left(store_query[ind],score)
        answer.append(cnt)
    

    return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])