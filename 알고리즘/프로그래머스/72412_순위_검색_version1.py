from itertools import combinations

def solution(info, query):
    answer = []
    languages = ['cpp','java','python','-']
    positions = ['backend','frontend','-']
    careers = ['junior','senior','-']
    soulfoods = ['chicken','pizza','-']
    total_dict = {language : {position : {career : {soulfood : [0]*100001 for soulfood in soulfoods} for career in careers}  for position in positions} for language in languages}
    for info_string in info:
        language,position,career,soulfood,score = info_string.split(' ')
        score = int(score)
        info_list = [language,position,career,soulfood]
        for i in range(1<<4):
            temp = []
            for j in range(4):
                if i&(1<<j):
                    temp.append(info_list[j])
                else:
                    temp.append('-')
            total_dict[temp[0]][temp[1]][temp[2]][temp[3]][score] += 1
    for language in total_dict.keys():
        for position in total_dict[language].keys():
            for career in total_dict[language][position].keys():
                for soulfood in total_dict[language][position][career].keys():
                    for score in range(1,100001):
                        total_dict[language][position][career][soulfood][score] += total_dict[language][position][career][soulfood][score-1]
    for query_string in query:
        language,position,career,last_query = map(str.strip,query_string.split('and'))
        soulfood,score = last_query.split(' ')
        score = int(score)
        answer.append(total_dict[language][position][career][soulfood][100000] - total_dict[language][position][career][soulfood][score-1])
    return answer



solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])