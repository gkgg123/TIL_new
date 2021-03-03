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
    store_query = [[0]*100001 for _ in range(108)]
    for info_string in info:
        language,position,career,soulfood,score = info_string.split(' ')
        score = int(score)
        for ind1 in [0,index_dict[language]]:
            for ind2 in [0,index_dict[position]]:
                for ind3 in [0,index_dict[career]]:
                    for ind4 in [0,index_dict[soulfood]]:
                        ind = ind1*27 + ind2*9 + ind3*3 + ind4
                        store_query[ind][score] += 1
    for ind in range(108):
        for score in range(1,100001):
            store_query[ind][score] += store_query[ind][score-1]

    for qu in query:
        language,position,career,last_query = map(str.strip,qu.split('and'))
        soulfood,score = last_query.split(' ')
        score = int(score)
        ind = index_dict[language]*27 + index_dict[position]*9 + index_dict[career]*3 + index_dict[soulfood]
        answer.append(store_query[ind][100000] - store_query[ind][score-1])
    

    return answer